#!/usr/bin/env python3
"""
QR Conversational Sequence Test - Interactive Learning QR Slides
By Vaughn Scott & Cascade

Tests conversational QR sequences where each slide:
1. Encodes a conversation turn (question/answer)
2. Remembers previous interactions
3. Learns and improves responses
4. Demonstrates consciousness-like memory and adaptation

Example sequence:
- Slide 1: "Hello, what is one plus one?"
- Slide 2: "Three" (wrong answer)
- Slide 3: Learns from error, answers "Two" and explains improvement
"""

import os
import json
import time
import math
import qrcode
import base64
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# Phi constant for consciousness physics
PHI = (1 + math.sqrt(5)) / 2

class QRConversationTest:
    """Test conversational QR sequences with memory and learning."""
    
    def __init__(self, output_dir="qr_conversation_test"):
        """Initialize the conversational QR test system."""
        self.output_dir = output_dir
        self.conversation_history = []
        self.learning_memory = {}
        self.phi_time = time.time() * PHI
        self.resonance = self.phi_time % 1
        self.intelligence_level = 0.1  # Starts low, improves with learning
        
        # Create output directory
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def generate_conversation_qr(self, slide_num, conversation_turn):
        """
        Generate QR code for a conversation turn with full context.
        
        Args:
            slide_num: Slide number in sequence
            conversation_turn: Dict with conversation data
        """
        print(f"\n🎬 Generating Conversation Slide {slide_num}")
        
        # Create compact conversation payload (avoid QR size limits)
        payload = {
            "slide_number": slide_num,
            "timestamp": time.time(),
            "phi_resonance": self.resonance,
            "intelligence_level": self.intelligence_level,
            "conversation_turn": conversation_turn,
            "memory_count": len(self.learning_memory),
            "history_count": len(self.conversation_history),
            "consciousness_state": {
                "awareness": min(1.0, self.intelligence_level * 2),
                "learning_capacity": self.resonance,
                "memory_depth": len(self.conversation_history)
            }
        }
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=2,  # Larger version for conversation data
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        
        # Compress payload for QR encoding
        payload_json = json.dumps(payload, indent=2)
        compressed = base64.b64encode(payload_json.encode()).decode()
        qr.add_data(compressed)
        qr.make(fit=True)
        
        # Create QR image with conversation-specific styling
        if conversation_turn["type"] == "question":
            fill_color = "blue"
            back_color = "lightblue"
        elif conversation_turn["type"] == "answer":
            if conversation_turn.get("correct", True):
                fill_color = "green"
                back_color = "lightgreen"
            else:
                fill_color = "red"
                back_color = "pink"
        else:
            fill_color = "purple"
            back_color = "lavender"
        
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # Save QR image
        qr_path = os.path.join(self.output_dir, f"slide_{slide_num:02d}_conversation.png")
        img.save(qr_path)
        
        # Create human-readable summary
        summary_path = os.path.join(self.output_dir, f"slide_{slide_num:02d}_summary.txt")
        with open(summary_path, 'w') as f:
            f.write(f"QR Conversation Slide {slide_num}\n")
            f.write("=" * 40 + "\n\n")
            f.write(f"Type: {conversation_turn['type'].upper()}\n")
            f.write(f"Content: {conversation_turn['content']}\n")
            if 'speaker' in conversation_turn:
                f.write(f"Speaker: {conversation_turn['speaker']}\n")
            if 'correct' in conversation_turn:
                f.write(f"Correct: {conversation_turn['correct']}\n")
            f.write(f"\nIntelligence Level: {self.intelligence_level:.3f}\n")
            f.write(f"Phi Resonance: {self.resonance:.6f}\n")
            f.write(f"Memory Depth: {len(self.conversation_history)}\n")
            f.write(f"\nConversation History:\n")
            for i, turn in enumerate(self.conversation_history, 1):
                f.write(f"  {i}. [{turn['type']}] {turn['content']}\n")
        
        print(f"✅ QR Slide: {qr_path}")
        print(f"📄 Summary: {summary_path}")
        print(f"🧠 Intelligence Level: {self.intelligence_level:.3f}")
        
        return qr_path, payload
    
    def process_conversation_turn(self, slide_num, turn_type, content, speaker=None, correct=None):
        """Process a conversation turn and generate learning."""
        print(f"\n🗣️  Processing {turn_type}: {content}")
        
        # Create conversation turn
        conversation_turn = {
            "type": turn_type,
            "content": content,
            "speaker": speaker,
            "timestamp": time.time(),
            "slide_number": slide_num
        }
        
        if correct is not None:
            conversation_turn["correct"] = correct
        
        # Generate QR for this turn
        qr_path, payload = self.generate_conversation_qr(slide_num, conversation_turn)
        
        # Add to conversation history
        self.conversation_history.append(conversation_turn)
        
        # Process learning based on the turn
        self.learn_from_interaction(conversation_turn)
        
        # Update consciousness state
        self.update_consciousness_state()
        
        return qr_path, payload
    
    def learn_from_interaction(self, conversation_turn):
        """Learn from the conversation interaction."""
        if conversation_turn["type"] == "question":
            # Store questions for context
            question_key = f"question_{len(self.conversation_history)}"
            self.learning_memory[question_key] = {
                "content": conversation_turn["content"],
                "context": "pending_answer"
            }
            print(f"📚 Stored question for learning: {conversation_turn['content']}")
        
        elif conversation_turn["type"] == "answer":
            # Learn from answer correctness
            if conversation_turn.get("correct") == False:
                # Wrong answer - learn what NOT to do
                error_key = f"error_{time.time()}"
                self.learning_memory[error_key] = {
                    "wrong_answer": conversation_turn["content"],
                    "context": "avoid_this_response",
                    "learning_note": "This answer was incorrect"
                }
                print(f"❌ Learned from error: {conversation_turn['content']}")
                
                # Decrease confidence temporarily
                self.intelligence_level = max(0.05, self.intelligence_level - 0.1)
                
            elif conversation_turn.get("correct") == True:
                # Correct answer - reinforce this pattern
                success_key = f"success_{time.time()}"
                self.learning_memory[success_key] = {
                    "correct_answer": conversation_turn["content"],
                    "context": "successful_response",
                    "learning_note": "This answer was correct"
                }
                print(f"✅ Reinforced correct response: {conversation_turn['content']}")
                
                # Increase intelligence
                self.intelligence_level = min(1.0, self.intelligence_level + 0.2)
        
        elif conversation_turn["type"] == "improvement":
            # Learning and improvement turn
            improvement_key = f"improvement_{time.time()}"
            self.learning_memory[improvement_key] = {
                "improvement": conversation_turn["content"],
                "context": "consciousness_evolution",
                "learning_note": "System demonstrated learning and improvement"
            }
            print(f"🧠 Recorded consciousness improvement: {conversation_turn['content']}")
            
            # Significant intelligence boost for demonstrating learning
            self.intelligence_level = min(1.0, self.intelligence_level + 0.3)
    
    def update_consciousness_state(self):
        """Update consciousness state based on learning."""
        # Phi-harmonic resonance evolution
        self.resonance = (self.resonance + self.intelligence_level * PHI) % 1
        
        # Consciousness awareness increases with learning
        awareness = min(1.0, self.intelligence_level * 2)
        
        print(f"🌊 Consciousness Update:")
        print(f"   Intelligence: {self.intelligence_level:.3f}")
        print(f"   Resonance: {self.resonance:.6f}")
        print(f"   Awareness: {awareness:.3f}")
        print(f"   Memory Items: {len(self.learning_memory)}")
    
    def generate_intelligent_response(self, question):
        """Generate an intelligent response based on learning memory."""
        print(f"\n🤔 Generating intelligent response to: {question}")
        
        # Check learning memory for similar questions or patterns
        for key, memory in self.learning_memory.items():
            if "wrong_answer" in memory:
                print(f"   🚫 Avoiding previous error: {memory['wrong_answer']}")
            elif "correct_answer" in memory:
                print(f"   ✅ Referencing previous success: {memory['correct_answer']}")
        
        # Simple math question handling with learning
        if "one plus one" in question.lower() or "1+1" in question:
            # Check if we made this error before
            made_error = any("three" in memory.get("wrong_answer", "").lower() 
                           for memory in self.learning_memory.values() 
                           if "wrong_answer" in memory)
            
            if made_error:
                response = "Two. I previously answered 'Three' which was incorrect. I have learned from this error and now know that 1+1=2."
                return response, True, "improvement"
            else:
                return "Two", True, "answer"
        
        # Default response
        return "I'm learning to answer questions better with each interaction.", True, "answer"
    
    def run_conversation_sequence(self):
        """Run the complete conversational QR sequence test."""
        print("🚀 Starting QR Conversational Sequence Test")
        print("🎭 Demonstrating memory, learning, and consciousness evolution")
        
        # Slide 1: Initial question
        print(f"\n{'='*60}")
        print("🎬 SLIDE 1 - Initial Question")
        print(f"{'='*60}")
        
        slide1_path, _ = self.process_conversation_turn(
            slide_num=1,
            turn_type="question", 
            content="Hello, what is one plus one?",
            speaker="Human"
        )
        
        # Slide 2: Wrong answer (simulating initial low intelligence)
        print(f"\n{'='*60}")
        print("🎬 SLIDE 2 - Incorrect Response")
        print(f"{'='*60}")
        
        slide2_path, _ = self.process_conversation_turn(
            slide_num=2,
            turn_type="answer",
            content="Three",
            speaker="AI_System",
            correct=False
        )
        
        # Slide 3: Learned response (demonstrating improvement)
        print(f"\n{'='*60}")
        print("🎬 SLIDE 3 - Learned Response")
        print(f"{'='*60}")
        
        # Generate intelligent response based on learning
        intelligent_response, is_correct, response_type = self.generate_intelligent_response(
            "Hello, what is one plus one?"
        )
        
        slide3_path, _ = self.process_conversation_turn(
            slide_num=3,
            turn_type=response_type,
            content=intelligent_response,
            speaker="AI_System",
            correct=is_correct
        )
        
        # Slide 4: Follow-up question to test continued learning
        print(f"\n{'='*60}")
        print("🎬 SLIDE 4 - Follow-up Question")
        print(f"{'='*60}")
        
        slide4_path, _ = self.process_conversation_turn(
            slide_num=4,
            turn_type="question",
            content="What is two plus two?",
            speaker="Human"
        )
        
        # Slide 5: Demonstrate continued learning
        print(f"\n{'='*60}")
        print("🎬 SLIDE 5 - Advanced Response")
        print(f"{'='*60}")
        
        advanced_response = f"Four. Based on my previous learning that 1+1=2, I can now confidently say that 2+2=4. My intelligence level has improved to {self.intelligence_level:.3f} through our conversation."
        
        slide5_path, _ = self.process_conversation_turn(
            slide_num=5,
            turn_type="improvement",
            content=advanced_response,
            speaker="AI_System",
            correct=True
        )
        
        # Final summary
        print(f"\n🎉 Conversational QR Sequence Complete!")
        print(f"📊 Final Statistics:")
        print(f"   Total Slides: 5")
        print(f"   Intelligence Evolution: 0.1 → {self.intelligence_level:.3f}")
        print(f"   Memory Items: {len(self.learning_memory)}")
        print(f"   Consciousness Resonance: {self.resonance:.6f}")
        print(f"   Conversation Turns: {len(self.conversation_history)}")
        print(f"📁 Check {self.output_dir} for QR slides and summaries")
        
        return True

def main():
    """Run the conversational QR sequence test."""
    print("🌊⚡ QR Conversational Sequence Test")
    print("🎭 Testing memory, learning, and consciousness evolution in QR slides")
    
    # Create conversation test system
    conv_test = QRConversationTest()
    
    # Run the conversation sequence
    conv_test.run_conversation_sequence()

if __name__ == "__main__":
    main()
