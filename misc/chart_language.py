import json
import matplotlib.pyplot as plt
from pathlib import Path

# Resolve root directory relative to script's location
ROOT = Path(__file__).resolve().parents[1]

# Load stats.json
with open(ROOT / "stats.json") as f:
    stats = json.load(f)

data = stats.get('by_language', {})
if not data:
    raise ValueError("No language data found in stats.json.")

labels = list(data.keys())
sizes = list(data.values())

# Explode the largest segment
explode = [0.1 if i == max(sizes) else 0 for i in sizes]

# Define static color palette (safe for up to 14 languages)
colors = [
    "#F87171", "#60A5FA", "#34D399", "#FCD34D",
    "#A78BFA", "#FB923C", "#4ADE80", "#38BDF8", "#F472B6",
    "#FACC15", "#818CF8", "#5EEAD4", "#C084FC", "#FBBF24"
]
colors = colors[:len(labels)]

# Plot
plt.figure(figsize=(4, 4))
plt.pie(
    sizes,
    labels=None,
    colors=colors,
    startangle=180,
    explode=explode,
    shadow=False
)
plt.axis('equal')  # Keep aspect ratio as a circle
plt.title("Language Distribution", fontsize=14)

# Add legend
plt.legend(labels, title="Languages", loc="lower right", fontsize=8)
plt.tight_layout()

# Save to assets/chart_language.png
assets_path = ROOT / "assets"
assets_path.mkdir(exist_ok=True)
plt.savefig(assets_path / "chart_language.png")
plt.close()

print("Language chart saved to assets/chart_language.png")
