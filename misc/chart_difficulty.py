import json
import matplotlib.pyplot as plt
from pathlib import Path

# Define root directory (one level above /misc)
ROOT = Path(__file__).resolve().parents[1]

# Load stats.json from the root
with open(ROOT / "stats.json") as f:
    stats = json.load(f)

# Use the leetcode_only section of the stats
diffs = stats['leetcode_only']

# Difficulty labels and corresponding values
labels = ['Easy', 'Medium', 'Hard']
values = [
    diffs.get('01_easy', 0),
    diffs.get('02_medium', 0),
    diffs.get('03_hard', 0)
]
colors = ['green', 'orange', 'red']

# Plotting
plt.figure(figsize=(4, 4))
plt.bar(labels, values, color=colors)

plt.title("Difficulty Breakdown (Leetcode Only)", fontsize=14)
plt.ylabel("Number of Problems", fontsize=11)
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)

# Save output to assets/chart_difficulty.png
assets_dir = ROOT / "assets"
assets_dir.mkdir(exist_ok=True)
plt.savefig(assets_dir / "chart_difficulty.png", bbox_inches='tight')
plt.close()

print("Difficulty chart saved to assets/chart_difficulty.png")
