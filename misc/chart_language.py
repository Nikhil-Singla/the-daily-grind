import json
import matplotlib.pyplot as plt
from pathlib import Path

with open("stats.json") as f:
    stats = json.load(f)

data = stats['by_language']
labels = list(data.keys())
sizes = list(data.values())
colors = ['#3572A5', '#f1e05a', '#4F5D95', '#3178c6']  # C++, Python, SQL, JS/TS

fig = plt.figure(figsize=(5, 4), dpi=100)
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 10})
plt.axis('equal')  # Keep it circular
plt.title('Language Distribution', fontsize=14)

Path("assets").mkdir(exist_ok=True)
fig.savefig("assets/chart_language.svg", format="svg", bbox_inches="tight", pad_inches=0)
plt.close()
