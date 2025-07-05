import json
from pathlib import Path
import re
import sys

# Load stats.json
stats_path = Path("stats.json")
if not stats_path.exists():
    print("stats.json not found.")
    sys.exit(1)

stats = json.load(stats_path.open("r", encoding="utf-8"))

# Difficulty label map (your folder prefixes to readable labels)
difficulty_labels = {
    "01_easy": "Easy",
    "02_medium": "Medium",
    "03_hard": "Hard"
}

# Build the difficulty breakdown section
difficulty_lines = "\n".join([
    f"- {label}: {stats['by_difficulty'].get(key, 0)}"
    for key, label in difficulty_labels.items()
])

# Format language usage line
language_lines = ", ".join([
    f"{lang} ({count})"
    for lang, count in stats['by_language'].items()
])

# Final stats block to inject
summary_block = f"""
- **Total Problems Solved**: {stats['total']}
- **Languages Used**: {language_lines}
- **Difficulty Breakdown**:
{difficulty_lines}
""".strip()

# Load README.md
readme_path = Path("README.md")
if not readme_path.exists():
    print("README.md not found.")
    sys.exit(1)

readme_content = readme_path.read_text(encoding="utf-8")

# Marker tags for stats block
start_tag = r"<!-- STATS:START -->"
end_tag = r"<!-- STATS:END -->"
pattern = rf"{start_tag}(.*?){end_tag}"

# Inject the block
if re.search(pattern, readme_content, re.DOTALL):
    new_readme = re.sub(
        pattern,
        f"{start_tag}\n{summary_block}\n{end_tag}",
        readme_content,
        flags=re.DOTALL
    )
    print("Stats section replaced successfully.")
else:
    print("STATS markers not found. Appending block at the end of README.")
    new_readme = readme_content.strip() + f"\n\n{start_tag}\n{summary_block}\n{end_tag}"

# Write the updated README
readme_path.write_text(new_readme, encoding="utf-8")
