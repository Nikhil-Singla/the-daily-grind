import os
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]

PLATFORMS = ['leetcode', 'hacker_rank']
DIFFICULTY_KEYS = ['01_easy', '02_medium', '03_hard']
VALID_EXTENSIONS = ['.py', '.cpp', '.js', '.ts', '.sql']

# Extension-to-language mapping
EXT_TO_LANG = {
    '.py': 'python',
    '.cpp': 'cpp',
    '.js': 'js_ts',
    '.ts': 'js_ts',
    '.sql': 'mysql'
}

def get_subfolders(path: Path):
    return [f.name for f in path.iterdir() if f.is_dir()]

def count_leetcode_problems(path: Path):
    counts = {key: 0 for key in DIFFICULTY_KEYS}
    lang_total = 0
    ext_counts = defaultdict(int)

    for diff in DIFFICULTY_KEYS:
        diff_path = path / diff
        if diff_path.exists():
            for f in diff_path.iterdir():
                if f.is_file() and f.suffix in VALID_EXTENSIONS:
                    counts[diff] += 1
                    ext = f.suffix
                    ext_counts[EXT_TO_LANG.get(ext, 'other')] += 1
                    lang_total += 1

    return counts, ext_counts, lang_total

def count_hacker_rank_problems(path: Path):
    count = 0
    ext_counts = defaultdict(int)

    for root, _, files in os.walk(path):
        for file in files:
            ext = Path(file).suffix
            if ext in VALID_EXTENSIONS:
                lang = EXT_TO_LANG.get(ext, 'other')
                ext_counts[lang] += 1
                count += 1

    return count, ext_counts

def count_total_all_files(root_path: Path):
    count = 0
    for path, _, files in os.walk(root_path):
        for file in files:
            if Path(file).suffix in VALID_EXTENSIONS:
                count += 1
    return count

# Folder structure detection
STRUCTURE = {platform: get_subfolders(ROOT / platform) for platform in PLATFORMS}

# Final stats object
stats = {
    'platforms': {},
    'total': 0,
    'by_language': defaultdict(int),
    'leetcode_only': {key: 0 for key in DIFFICULTY_KEYS},
    'hacker_rank_only': {}
}

# Leetcode section
for lang_folder in STRUCTURE['leetcode']:
    path = ROOT / 'leetcode' / lang_folder
    if not path.exists():
        continue

    lang_key = f"leetcode/{lang_folder}"
    diff_counts, ext_counts, total_files = count_leetcode_problems(path)
    stats['platforms'][lang_key] = diff_counts

    for diff, count in diff_counts.items():
        stats['leetcode_only'][diff] += count

    for lang, count in ext_counts.items():
        stats['by_language'][lang] += count

# HackerRank section
for topic_folder in STRUCTURE['hacker_rank']:
    path = ROOT / 'hacker_rank' / topic_folder
    if not path.exists():
        continue

    count, ext_counts = count_hacker_rank_problems(path)
    stats['platforms'][f"hacker_rank/{topic_folder}"] = count
    stats['hacker_rank_only'][topic_folder] = count

    for lang, cnt in ext_counts.items():
        stats['by_language'][lang] += cnt

# Final total
stats['total'] = (
    count_total_all_files(ROOT / 'leetcode') +
    count_total_all_files(ROOT / 'hacker_rank')
)

# Convert defaultdict to dict before saving
stats['by_language'] = dict(stats['by_language'])

# Save
with open(ROOT / 'stats.json', 'w') as f:
    json.dump(stats, f, indent=2)

print("stats.json updated successfully.")
