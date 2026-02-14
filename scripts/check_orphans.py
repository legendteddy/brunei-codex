import os
import re
from collections import defaultdict
from pathlib import Path

def scan_links():
    guides_dir = Path("g:/My Drive/BruneiVerse/_guides")
    link_pattern = re.compile(r"\]\(\{\{\s*['\"]/guides/([^/]+)/['\"]\s*\|\s*relative_url\s*\}\}\)")
    
    # Map slug -> incoming_count
    incoming_counts = defaultdict(int)
    all_slugs = set()

    # 1. Get all guides
    for f in guides_dir.glob("*.md"):
        slug = f.stem 
        all_slugs.add(slug)

    # 2. Scan all files for links TO these slugs
    # We scan _guides, but also potentially other pages if they exist. 
    # For now, let's focus on inter-guide linking density.
    dataset = list(guides_dir.glob("*.md"))
    
    print(f"Scanning {len(dataset)} guides for internal links...")

    for f in dataset:
        content = f.read_text(encoding="utf-8")
        # Check for standard markdown links too just in case: ](/guides/slug/)
        # Regex for Jekyll relative_url
        jekyll_matches = link_pattern.findall(content)
        for target_slug in jekyll_matches:
            incoming_counts[target_slug] += 1
            
        # Regex for raw paths if any
        raw_matches = re.findall(r"\]\(/guides/([^/]+)/?\)", content)
        for target_slug in raw_matches:
            incoming_counts[target_slug] += 1

    # 3. Report Orphans (0 links) and Low Density (< 3 links)
    orphans = []
    low_density = []
    
    print(f"\nLink Audit Results:")
    print(f"{'Slug':<50} | {'Incoming Links'}")
    print("-" * 70)
    
    for slug in sorted(all_slugs):
        count = incoming_counts.get(slug, 0)
        print(f"{slug:<50} | {count}")
        if count == 0:
            orphans.append(slug)
        elif count < 3:
            low_density.append(slug)

    print("-" * 70)
    print(f"\nOrphans (0 incoming): {len(orphans)}")
    for o in orphans:
        print(f" - {o}")
        
    print(f"\nLow Density (< 3 incoming): {len(low_density)}")
    for l in low_density:
        print(f" - {l}")

if __name__ == "__main__":
    scan_links()
