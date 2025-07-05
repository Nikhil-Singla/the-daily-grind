import json
from pathlib import Path
import re

stats = json.load(open("stats.json"))

summary = f"""- **Total Problems Solved:** {stats['total']}
- **Languages Used:** {', '.join([f"{lang} ({count})" for lang, count in stats['by_language'].items()])}
- **Difficulty Breakdown:**
  - 🟢 Easy: {stats['by_difficulty']['easy']}
  - 🟠 Medium: {stats['by_difficulty']['medium']}
  - 🔴 Hard: {stats['by_difficulty']['hard']}
"""

readme_path = Path("README.md")
content = readme_path.read_text()

# Replace STATS block
new_content = re.sub(
    r"<!-- STATS:START -->(.*?)<!-- STATS:END -->",
    f"<!-- STATS:START -->\n{summary}\n<!-- STATS:END -->",
    content,
    flags=re.DOTALL
)

readme_path.write_text(new_content)
