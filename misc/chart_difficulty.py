import json
import matplotlib.pyplot as plt
from pathlib import Path

with open("stats.json") as f:
    stats = json.load(f)

diffs = stats['by_difficulty']
labels = diffs.keys()
values = diffs.values()

colors = ['green', 'orange', 'red']

plt.bar(labels, values, color=colors)
plt.title("Difficulty Breakdown")
plt.ylabel("Number of Problems")
plt.tight_layout()
Path("assets").mkdir(exist_ok=True)
plt.savefig("assets/chart_difficulty.svg")
