#!/usr/bin/env python3
"""
Script to download Google Sheets as CSV files.
This uses the public CSV export feature (no authentication needed).
"""

import os
import urllib.request
from datetime import datetime

# Google Sheets ID
SHEET_ID = os.getenv('SHEET_ID', '15aKwZohEpEwa9fOOnrcqZvAQ-JdHrVLcRTKglM2g1EQ')

# Sheet tab names and their GIDs
SHEETS = {
    'dungeon_boss_material.csv': 257026824,
    'title_tracker.csv': 1925983488
}

def download_sheet_as_csv(sheet_id, gid, output_filename):
    """Download a specific sheet tab as CSV"""
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}'
    
    print(f"Downloading {output_filename} from Google Sheets...")
    try:
        urllib.request.urlretrieve(url, output_filename)
        print(f"✓ Successfully saved {output_filename}")
        return True
    except Exception as e:
        print(f"✗ Error downloading {output_filename}: {e}")
        return False

def main():
    print(f"Starting sync at {datetime.utcnow().isoformat()} UTC")
    print(f"Sheet ID: {SHEET_ID}\n")
    
    success_count = 0
    
    # Download each sheet
    for filename, gid in SHEETS.items():
        if download_sheet_as_csv(SHEET_ID, gid, filename):
            success_count += 1
    
    print(f"\nSync complete: {success_count}/{len(SHEETS)} sheets downloaded")
    return 0 if success_count == len(SHEETS) else 1

if __name__ == '__main__':
    exit(main())
