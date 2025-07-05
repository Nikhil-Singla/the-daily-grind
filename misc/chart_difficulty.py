import json
import matplotlib.pyplot as plt
from pathlib import Path

with open("stats.json") as f:
    stats = json.load(f)

diffs = stats['by_difficulty']
labels = ['Easy', 'Medium', 'Hard']
values = [
    diffs.get('01_easy', 0),
    diffs.get('02_medium', 0),
    diffs.get('03_hard', 0)
]
colors = ['green', 'orange', 'red']

fig = plt.figure(figsize=(5, 4), dpi=100)
plt.bar(labels, values, color=colors)
plt.title("Difficulty Breakdown", fontsize=14)
plt.ylabel("Number of Problems", fontsize=11)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

Path("assets").mkdir(exist_ok=True)
fig.savefig("assets/chart_difficulty.svg", format="svg", bbox_inches="tight", pad_inches=0)
plt.close()
