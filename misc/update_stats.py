import os
import json
from pathlib import Path

# Get the root directory of the project
# Assuming this script is in misc/update_stats.py, we go two levels up to get the root
ROOT = Path(__file__).resolve().parents[1]

# print(ROOT)

# Languages and platforms to support
STRUCTURE = {
    'leetcode': ['cpp', 'python', 'js_ts', 'mysql'],
    'hackerrank': ['problem_solving', 'python']
}

def countProblems(baseFolder):

    # Folderlist refers to the folder naming convention used
    # Each repository has three folders for different difficulty levels
    folderList = {'01_easy': 0, '02_medium': 0, '03_hard': 0}
    
    for difficulty in folderList:

        # Append the difficulty level (following the folder naming convention) to the base folder
         
        diffDirectory = baseFolder / difficulty

        # Check if the directory exists

        if diffDirectory.exists():
            
            folderList[difficulty] = len([
                # List all files in the directory that match the specified extensions
                oneFile for oneFile in diffDirectory.iterdir() if (oneFile.is_file() and oneFile.suffix in ['.py', '.cpp', '.js', '.ts', '.sql'])                
            ])

    return folderList

stats = {'platforms': {}, 'total': 0, 'by_language': {}, 'by_difficulty': {'01_easy': 0, '02_medium': 0, '03_hard': 0}}

for platformWebsite, languagesUsed in STRUCTURE.items():

    for oneLanguage in languagesUsed:
        
        path = ROOT / platformWebsite / oneLanguage
        if not path.exists():
            continue

        langKey = f"{platformWebsite}/{oneLanguage}"

        difficultyCounter = countProblems(path)

        stats['platforms'][langKey] = difficultyCounter

        for diff, count in difficultyCounter.items():
            
            stats['total'] += count
            stats['by_difficulty'][diff] += count
            stats['by_language'].setdefault(oneLanguage, 0)
            stats['by_language'][oneLanguage] += count

# Save to stats.json at root
with open(ROOT / 'stats.json', 'w') as f:
    json.dump(stats, f, indent=2)


