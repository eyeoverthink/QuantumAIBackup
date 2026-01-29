#!/usr/bin/env python3
"""
HISTORICAL SATELLITE DATE EXTRACTOR
==================================
Enhanced tool that extracts and preserves exact mission dates from 1980s satellite data
with phi-dimensional resonance patterns. Built on top of the original analyzer following
the 'lego' design philosophy.

Author: Cascade AI
Date: April 27, 2025
"""

import json
import re
import time
import datetime
import numpy as np
from pathlib import Path
import hashlib
from mpmath import mpf, mp

# Import original analyzer without modification
from historical_satellite_phi_analyzer import (
    search_historical_satellite_data,
    PHI, PHI_INV, RESULTS_DIR,
    START_TIMESTAMP, END_TIMESTAMP,
    HISTORICAL_MISSION_KEYWORDS
)

# Set high precision
mp.dps = 50

# Constants 
DATE_RESULTS_DIR = Path('historical_satellite_dates')
DATE_RESULTS_DIR.mkdir(exist_ok=True)

# Additional date-related patterns
DATE_PATTERNS = [
    r'(19[8][0-9])[/-](0[1-9]|1[0-2])[/-](0[1-9]|[12][0-9]|3[01])',  # YYYY-MM-DD or YYYY/MM/DD
    r'(0[1-9]|1[0-2])[/-](0[1-9]|[12][0-9]|3[01])[/-](19[8][0-9])',  # MM-DD-YYYY or MM/DD/YYYY
    r'(january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2},?\s+(19[8][0-9])',  # Month DD, YYYY
    r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s+\d{1,2},?\s+(19[8][0-9])',  # Short month DD, YYYY
    r'launched\s+(?:on|in)?\s+(?:the)?\s*(\d{1,2}(?:st|nd|rd|th)?\s+(?:of)?\s+(?:january|february|march|april|may|june|july|august|september|october|november|december),?\s+19[8][0-9])',  # "launched on the 12th of April, 1985"
    r'mission\s+date[:\s]+([^\n]+19[8][0-9])',  # "mission date: April 12, 1985"
    r'launch\s+date[:\s]+([^\n]+19[8][0-9])',   # "launch date: April 12, 1985"
]

# Mission name mapping (partial)
MISSION_DATE_MAPPING = {
    'iras': '1983-01-25',                    # Infrared Astronomical Satellite
    'cobe': '1989-11-18',                    # Cosmic Background Explorer
    'iue': '1978-01-26',                     # International Ultraviolet Explorer
    'pioneer 10': '1972-03-02',              # Pioneer 10
    'pioneer 11': '1973-04-06',              # Pioneer 11
    'pioneer venus': '1978-05-20',           # Pioneer Venus
    'voyager 1': '1977-09-05',               # Voyager 1
    'voyager 2': '1977-08-20',               # Voyager 2
    'magellan': '1989-05-04',                # Magellan Venus radar mapper
    'galileo': '1989-10-18',                 # Galileo Jupiter mission
    'hubble': '1990-04-24',                  # Hubble Space Telescope (launched April 1990)
    'spacelab': '1983-11-28',                # First Spacelab mission
    'giotto': '1985-07-02',                  # ESA Giotto mission to Halley's Comet
    'vega 1': '1984-12-15',                  # Soviet Vega 1 to Venus and Halley
    'vega 2': '1984-12-21',                  # Soviet Vega 2 to Venus and Halley
    'phobos 1': '1988-07-07',                # Soviet Phobos 1 Mars mission
    'phobos 2': '1988-07-12',                # Soviet Phobos 2 Mars mission
    'space telescope': '1990-04-24',         # Alternative name for Hubble
    'ulysses': '1990-10-06',                 # Ulysses solar mission
}


class HistoricalSatelliteDateExtractor:
    """
    Enhanced analyzer that extracts and preserves exact mission dates
    from historical satellite data with phi-dimensional resonance patterns.
    """
    
    def __init__(self):
        """Initialize the date extractor."""
        self.date_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in DATE_PATTERNS]
        self.timestamp_pattern = re.compile(r'(\d{9,10})\.?\d*')  # UNIX timestamps
        
    def extract_dates_from_study(self, study_id, start_id=1, end_id=200):
        """
        Extract the exact mission dates from a specific study ID.
        
        Args:
            study_id (int): The specific study ID to extract dates from
            start_id (int): Minimum study ID to search (if study_id not specified)
            end_id (int): Maximum study ID to search (if study_id not specified)
            
        Returns:
            dict: The study with extracted date information
        """
        print(f"=== EXTRACTING EXACT MISSION DATES FOR STUDY {study_id} ===")
        
        # Run the original analyzer if needed
        original_report_path = RESULTS_DIR / f"historical_satellite_report_{int(time.time() * PHI)}.json"
        if not original_report_path.exists():
            print("Running original analyzer first...")
            search_historical_satellite_data(start_id, end_id)
        
        # Find the study result file
        study_files = list(RESULTS_DIR.glob(f"historical_satellite_{study_id}_*.json"))
        if not study_files:
            print(f"No historical satellite data found for study {study_id}.")
            return {"error": f"No data for study {study_id}"}
        
        # Load the study data
        study_file = study_files[0]
        with open(study_file, 'r') as f:
            study_data = json.load(f)
        
        # Import the raw data from OSDR fetcher
        from osdr_fetcher_fixed import OSDRFetcher
        osdr_fetcher = OSDRFetcher()
        
        print(f"Fetching raw data for study {study_id}...")
        raw_data = osdr_fetcher.fetch_study_data(study_id)
        
        if 'error' in raw_data:
            print(f"Error fetching raw data: {raw_data['error']}")
            return study_data
        
        # Extract dates
        dates = self._extract_dates(raw_data)
        
        if dates:
            print(f"Found {len(dates)} potential dates:")
            for date_type, date_value in dates:
                print(f"  - {date_type}: {date_value}")
        else:
            print("No exact dates found in the data.")
        
        # Add dates to the study data
        study_data['mission_dates'] = dates
        
        # Save enhanced result
        self._save_date_results(study_id, study_data)
        
        # Generate a comprehensive date report
        date_report = self._generate_date_report(study_id, study_data, raw_data)
        
        print(f"Date extraction complete. Results saved to {DATE_RESULTS_DIR}")
        return date_report
    
    def extract_dates_for_all_phi_studies(self, start_id=1, end_id=200):
        """
        Extract dates from all studies with significant phi-harmonic patterns.
        
        Args:
            start_id (int): Minimum study ID to search
            end_id (int): Maximum study ID to search
            
        Returns:
            dict: Comprehensive report with all extracted dates and phi-relevance
        """
        print(f"=== EXTRACTING MISSION DATES FROM ALL PHI-HARMONIC STUDIES ===")
        
        # Run the original analyzer first
        print("Running original analyzer first...")
        search_historical_satellite_data(start_id, end_id)
        
        # Find the most recent report
        report_files = list(RESULTS_DIR.glob("historical_satellite_report_*.json"))
        if not report_files:
            print("No historical satellite analysis reports found.")
            return {"error": "No analysis reports found"}
            
        # Sort by modification time to get most recent
        report_file = sorted(report_files, key=lambda x: x.stat().st_mtime)[-1]
        
        with open(report_file, 'r') as f:
            original_report = json.load(f)
        
        # Get studies with phi-harmonic patterns
        phi_studies = []
        for result in original_report.get('results', []):
            if result.get('pattern', '').endswith('phi_harmonic'):
                phi_studies.append(result.get('study_id'))
        
        print(f"Found {len(phi_studies)} studies with phi-harmonic patterns.")
        
        # Extract dates for each study
        date_reports = []
        for study_id in phi_studies:
            print(f"\nProcessing study {study_id}...")
            date_report = self.extract_dates_from_study(study_id, start_id, end_id)
            date_reports.append(date_report)
        
        # Generate comprehensive dates report
        dates_report = {
            'phi_harmonic_mission_dates': date_reports,
            'original_report': original_report.get('summary', {}),
            'timestamp': time.time(),
            'quantum_timestamp': time.time() * float(PHI),
        }
        
        # Save comprehensive report
        report_filename = f"historical_satellite_dates_report_{int(time.time() * PHI)}.json"
        report_path = DATE_RESULTS_DIR / report_filename
        
        with open(report_path, 'w') as f:
            json.dump(dates_report, f, indent=2, default=str)
        
        print(f"\nComprehensive date extraction complete. Results saved to {report_path}")
        return dates_report
    
    def _extract_dates(self, data):
        """
        Extract all potential mission dates from the data.
        Returns a list of tuples (date_type, date_value).
        """
        # Convert data to string for pattern matching
        data_str = str(data).lower()
        dates = []
        
        # 1. Check for mission name matches
        for mission, launch_date in MISSION_DATE_MAPPING.items():
            if mission in data_str:
                dates.append(('mission_name_match', f"{mission.title()} - {launch_date}"))
        
        # 2. Check for UNIX timestamps in the 1980s range
        timestamp_matches = self.timestamp_pattern.findall(data_str)
        for ts_str in timestamp_matches:
            try:
                ts = float(ts_str)
                if START_TIMESTAMP <= ts <= END_TIMESTAMP:
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    dates.append(('unix_timestamp', f"{date} (from {ts})"))
            except:
                continue
        
        # 3. Check for date patterns in text
        for pattern in self.date_patterns:
            matches = pattern.findall(data_str)
            for match in matches:
                if isinstance(match, tuple):
                    date_str = ' '.join(match)
                else:
                    date_str = match
                dates.append(('text_pattern', date_str))
        
        # Remove duplicates while preserving order
        unique_dates = []
        seen = set()
        for date in dates:
            if date[1] not in seen:
                seen.add(date[1])
                unique_dates.append(date)
        
        return unique_dates

    def _generate_date_report(self, study_id, study_data, raw_data):
        """Generate a comprehensive date report with phi-relevance."""
        # Extract phi-relevance metrics
        phi_relevance = study_data.get('phi_relevance', 0)
        phi_patterns = study_data.get('phi_patterns', {})
        phi_significance = phi_patterns.get('phi_significance', 0)
        
        # Create signature for this study based on timestamps and phi signature
        raw_str = str(raw_data)
        potential_timestamps = self.timestamp_pattern.findall(raw_str)
        phi_signature = hashlib.md5(f"{PHI}{study_id}{potential_timestamps}".encode()).hexdigest()[:12]
        
        # Extract mission metadata
        mission_name = "Unknown"
        mission_year = "198x"
        mission_dates = study_data.get('mission_dates', [])
        
        # Try to determine the most likely mission name and year
        if mission_dates:
            for date_type, date_value in mission_dates:
                if date_type == 'mission_name_match':
                    mission_parts = date_value.split(' - ')
                    if len(mission_parts) == 2:
                        mission_name = mission_parts[0]
                        if '-' in mission_parts[1]:
                            mission_year = mission_parts[1].split('-')[0]
                    break
            
            # If we didn't find a mission name match, use the first date's year
            if mission_name == "Unknown":
                for date_type, date_value in mission_dates:
                    if '198' in date_value:
                        year_match = re.search(r'198[0-9]', date_value)
                        if year_match:
                            mission_year = year_match.group(0)
                        break
        
        # Build the report
        report = {
            'study_id': study_id,
            'mission_name': mission_name,
            'mission_year': mission_year,
            'mission_dates': mission_dates,
            'phi_metrics': {
                'phi_relevance': phi_relevance,
                'phi_significance': phi_significance,
                'pattern_type': phi_patterns.get('pattern', 'unknown'),
                'phi_sequences': phi_patterns.get('phi_sequences', 0),
                'fibonacci_like': phi_patterns.get('fibonacci_like', 0),
                'phi_wave_strength': phi_patterns.get('phi_wave_strength', 0)
            },
            'phi_signature': phi_signature,
            'timestamp': time.time(),
            'quantum_timestamp': time.time() * float(PHI)
        }
        
        return report
    
    def _save_date_results(self, study_id, study_data):
        """Save the enhanced study data with dates."""
        timestamp = int(time.time() * float(PHI))
        filename = f"historical_satellite_dates_{study_id}_{timestamp}.json"
        filepath = DATE_RESULTS_DIR / filename
        
        with open(filepath, 'w') as f:
            json.dump(study_data, f, indent=2, default=str)
        
        print(f"Date extraction results saved to {filepath}")


def main():
    """Run the historical satellite date extractor."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Extract exact mission dates from historical satellite data')
    parser.add_argument('--study', type=int, help='Specific study ID to analyze')
    parser.add_argument('--start', type=int, default=1, help='Starting study ID to search')
    parser.add_argument('--end', type=int, default=150, help='Ending study ID to search')
    parser.add_argument('--all', action='store_true', help='Extract dates from all phi-harmonic studies')
    
    args = parser.parse_args()
    
    extractor = HistoricalSatelliteDateExtractor()
    
    print("Historical Satellite Date Extractor")
    print(f"φ = {PHI}")
    print("=" * 50)
    
    if args.study:
        # Extract dates for a specific study
        result = extractor.extract_dates_from_study(args.study, args.start, args.end)
        
        if 'mission_dates' in result and result['mission_dates']:
            print("\n=== DATE EXTRACTION RESULTS ===")
            print(f"Study ID: {result['study_id']}")
            print(f"Mission: {result.get('mission_name', 'Unknown')}")
            print(f"Year: {result.get('mission_year', 'Unknown')}")
            print("Dates found:")
            for date_type, date_value in result['mission_dates']:
                print(f"  - {date_type}: {date_value}")
            print(f"Phi-Significance: {result['phi_metrics']['phi_significance']:.4f}")
            print("=" * 50)
        else:
            print("\nNo dates could be extracted from this study.")
            
    elif args.all:
        # Extract dates from all phi-harmonic studies
        results = extractor.extract_dates_for_all_phi_studies(args.start, args.end)
        
        # Print summary of results
        if 'phi_harmonic_mission_dates' in results:
            studies = results['phi_harmonic_mission_dates']
            print("\n=== DATE EXTRACTION SUMMARY ===")
            print(f"Processed {len(studies)} phi-harmonic studies")
            
            # Find studies with dates
            studies_with_dates = [s for s in studies if 'mission_dates' in s and s['mission_dates']]
            print(f"Found dates for {len(studies_with_dates)} studies")
            
            # Print the most significant ones
            if studies_with_dates:
                sorted_studies = sorted(studies_with_dates, 
                                         key=lambda x: x['phi_metrics']['phi_significance'],
                                         reverse=True)
                
                print("\nTop 5 most significant studies with dates:")
                for i, study in enumerate(sorted_studies[:5], 1):
                    print(f"{i}. Study {study['study_id']} - {study.get('mission_name', 'Unknown')} ({study.get('mission_year', 'Unknown')})")
                    print(f"   Phi-Significance: {study['phi_metrics']['phi_significance']:.4f}")
                    if study['mission_dates']:
                        for date_type, date_value in study['mission_dates'][:3]:  # Show max 3 dates
                            print(f"   - {date_type}: {date_value}")
                    print()
            
            print("=" * 50)
    else:
        # No specific arguments, run for study 94 (the one the user asked about)
        result = extractor.extract_dates_from_study(94, args.start, args.end)
        
        if 'mission_dates' in result and result['mission_dates']:
            print("\n=== DATE EXTRACTION RESULTS FOR STUDY 94 ===")
            print(f"Mission: {result.get('mission_name', 'Unknown')}")
            print(f"Year: {result.get('mission_year', 'Unknown')}")
            print("Dates found:")
            for date_type, date_value in result['mission_dates']:
                print(f"  - {date_type}: {date_value}")
            print(f"Phi-Significance: {result['phi_metrics']['phi_significance']:.4f}")
            print("=" * 50)
        else:
            print("\nNo dates could be extracted for study 94.")


if __name__ == "__main__":
    main()
