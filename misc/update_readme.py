import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
stats_path = ROOT / "stats.json"
readme_path = ROOT / "README.md"

# Load stats.json
if not stats_path.exists():
    print("stats.json not found.")
    sys.exit(1)

with stats_path.open("r", encoding="utf-8") as f:
    stats = json.load(f)

# Map folder names to human-readable labels
difficulty_labels = {
    "01_easy": "Easy",
    "02_medium": "Medium",
    "03_hard": "Hard"
}

# Format difficulty breakdown from leetcode_only
leetcode_difficulties = stats.get("leetcode_only", {})
difficulty_lines = "\n".join([
    f"  - {label}: {leetcode_difficulties.get(key, 0)}"
    for key, label in difficulty_labels.items()
])

# Format languages
language_lines = ", ".join([
    f"{lang} ({count})"
    for lang, count in stats.get("by_language", {}).items()
])

# Compose final block for README injection
summary_block = f"""- **Total Problems Solved**: {stats.get('total', 0)}
- **Languages Used**: {language_lines}
- **Leetcode Breakdown**:
{difficulty_lines}
"""

# Load README.md
if not readme_path.exists():
    print("README.md not found.")
    sys.exit(1)

readme_content = readme_path.read_text(encoding="utf-8")

# Replace between markers
start_tag = r"<!-- STATS:START -->"
end_tag = r"<!-- STATS:END -->"
pattern = rf"{start_tag}(.*?){end_tag}"

if re.search(pattern, readme_content, re.DOTALL):
    updated_content = re.sub(
        pattern,
        f"{start_tag}\n{summary_block}\n{end_tag}",
        readme_content,
        flags=re.DOTALL
    )
    print("STATS section updated.")
else:
    updated_content = readme_content.strip() + f"\n\n{start_tag}\n{summary_block}\n{end_tag}"
    print("STATS section not found. Appended at end of README.")

# Save back
readme_path.write_text(updated_content, encoding="utf-8")
