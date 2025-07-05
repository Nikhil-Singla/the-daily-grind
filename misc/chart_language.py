import json
import random
import matplotlib.pyplot as plt
from pathlib import Path

# Load counts from stats.json
with open("stats.json") as f:
    stats = json.load(f)

data = stats['by_language']

labels = list(data.keys())
sizes = list(data.values())

explode = [0] * len(labels)  
# Explode the maximum value

max_index = sizes.index(max(sizes))
explode[max_index] = 0.1

colors = [
    "#F87171", "#60A5FA", "#34D399", "#FCD34D",
    "#A78BFA", "#FB923C", "#4ADE80", "#38BDF8", "#F472B6",
    "#FACC15", "#818CF8", "#5EEAD4", "#C084FC", "#FBBF24"
]

# We get number of labels, and then randomly select that many colors, assuming there are enough colors
colors = colors[:len(labels)]

plt.figure(figsize=(4, 4))

plt.pie(sizes, colors=colors, startangle=180, explode=explode, shadow=True)

plt.axis('equal')  # Pie Circle
plt.title('Language Distribution')

# Want the legend to be snug with the border
plt.legend(labels, title="Languages", loc="lower right", fontsize=8)
plt.tight_layout()

Path("assets").mkdir(exist_ok=True)
plt.savefig("assets/chart_language.png")
