import asyncio
import aiohttp
import numpy as np
from typing import List, Dict, Any
from bs4 import BeautifulSoup
import json
import torch
from transformers import AutoTokenizer, AutoModel
import re
from urllib.parse import urljoin

class KnowledgeScraper:
    def __init__(self, model_name: str = "sentence-transformers/all-mpnet-base-v2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.knowledge_base = []
        self.embedding_cache = {}
        
    async def scrape_knowledge(self, urls: List[str], max_depth: int = 2):
        """Scrape knowledge from multiple URLs asynchronously"""
        async with aiohttp.ClientSession() as session:
            tasks = [self.process_url(session, url, depth=0, max_depth=max_depth) for url in urls]
            await asyncio.gather(*tasks)
            
    async def process_url(self, session: aiohttp.ClientSession, url: str, depth: int, max_depth: int):
        """Process a single URL and extract knowledge"""
        if depth >= max_depth:
            return
            
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    # Extract text content
                    text_content = self._extract_text(soup)
                    
                    # Extract code snippets
                    code_snippets = self._extract_code(soup)
                    
                    # Generate embeddings
                    embeddings = self._generate_embeddings(text_content)
                    
                    # Store knowledge
                    knowledge_item = {
                        'url': url,
                        'text': text_content,
                        'code': code_snippets,
                        'embeddings': embeddings,
                        'metadata': {
                            'depth': depth,
                            'timestamp': asyncio.get_event_loop().time()
                        }
                    }
                    self.knowledge_base.append(knowledge_item)
                    
                    # Find and process related URLs
                    if depth < max_depth:
                        related_urls = self._extract_related_urls(soup, url)
                        tasks = [
                            self.process_url(session, related_url, depth + 1, max_depth)
                            for related_url in related_urls[:5]  # Limit to 5 related URLs per page
                        ]
                        await asyncio.gather(*tasks)
                        
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")
            
    def _extract_text(self, soup: BeautifulSoup) -> str:
        """Extract meaningful text content from HTML"""
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
            
        # Get text and clean it
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        return text
        
    def _extract_code(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        """Extract code snippets from HTML"""
        code_snippets = []
        for code_block in soup.find_all('pre'):
            lang = code_block.get('class', [''])[0] if code_block.get('class') else ''
            code_snippets.append({
                'language': lang,
                'code': code_block.get_text()
            })
        return code_snippets
        
    def _generate_embeddings(self, text: str) -> torch.Tensor:
        """Generate embeddings for text using the language model"""
        if text in self.embedding_cache:
            return self.embedding_cache[text]
            
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
            embeddings = outputs.last_hidden_state.mean(dim=1)
            
        self.embedding_cache[text] = embeddings
        return embeddings
        
    def _extract_related_urls(self, soup: BeautifulSoup, base_url: str) -> List[str]:
        """Extract related URLs from the page"""
        related_urls = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                full_url = urljoin(base_url, href)
                if full_url.startswith(('http://', 'https://')):
                    related_urls.append(full_url)
        return list(set(related_urls))  # Remove duplicates
        
    def get_relevant_knowledge(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Retrieve relevant knowledge for a given query"""
        query_embedding = self._generate_embeddings(query)
        
        # Calculate similarities
        similarities = []
        for item in self.knowledge_base:
            similarity = torch.cosine_similarity(query_embedding, item['embeddings'])
            similarities.append((similarity.item(), item))
            
        # Sort by similarity and return top-k
        similarities.sort(key=lambda x: x[0], reverse=True)
        return [item for _, item in similarities[:top_k]]
        
    def save_knowledge_base(self, path: str):
        """Save the knowledge base to disk"""
        save_data = {
            'knowledge_base': [
                {k: v.tolist() if isinstance(v, torch.Tensor) else v 
                 for k, v in item.items()}
                for item in self.knowledge_base
            ],
            'embedding_cache': {
                k: v.tolist() for k, v in self.embedding_cache.items()
            }
        }
        with open(path, 'w') as f:
            json.dump(save_data, f)
            
    def load_knowledge_base(self, path: str):
        """Load the knowledge base from disk"""
        with open(path, 'r') as f:
            data = json.load(f)
            
        self.knowledge_base = [
            {k: torch.tensor(v) if k == 'embeddings' else v 
             for k, v in item.items()}
            for item in data['knowledge_base']
        ]
        self.embedding_cache = {
            k: torch.tensor(v) for k, v in data['embedding_cache'].items()
        }
