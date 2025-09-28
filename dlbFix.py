import os, re, shutil
from datetime import datetime

HTML_FILE = "index.html"

# New 3-column main block
NEW_MAIN = """
<main class="three-columns">
  <!-- About Section -->
  <section id="about">
    <h2>About</h2>
    <p>
      Our mission is to make the Word of God accessible with clarity and reverence.
      We combine scripture, history, and commentary into a format that is beautiful,
      functional, and faithful to the original text.
    </p>
  </section>

  <!-- Features Section -->
  <section id="features">
    <h2>Features</h2>
    <ul>
      <li>✓ Strong’s numbers with definitions.</li>
      <li>✓ Day, Sepia, and Night themes.</li>
      <li>✓ Search and navigation tools.</li>
      <li>✓ More features planned for future versions.</li>
    </ul>
  </section>

  <!-- Call to Action Section -->
  <section id="cta">
    <h2>Call to Action</h2>
    <p>
      Join us in preserving and sharing these resources.
      Your support helps ensure that Biblical truth remains accessible to all.
    </p>
  </section>
</main>
"""

# Updated CSS block for 33 | 34 | 33 split
CSS_BLOCK = """
main.three-columns {
  display: grid;
  grid-template-columns: 33% 34% 33%;
  gap: 20px;
  max-width: 1200px;
  margin: 20px auto;
  line-height: 1.5;
  text-align: left;
  align-items: start;
}
main.three-columns section {
  padding: 0 15px;
}
main.three-columns h2 {
  text-align: center;
  font-size: 1.4rem;
  font-weight: bold;
  margin-top: 0;
  margin-bottom: 0.5em;
}
main.three-columns p,
main.three-columns ul {
  text-align: left;
  margin: 0 0 1em;
}
"""

def backup_file(path):
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    bak = f"{path}.{ts}.bak"
    shutil.copy(path, bak)
    print(f"📂 Backup created: {bak}")
    return bak

def patch_index():
    if not os.path.exists(HTML_FILE):
        print("❌ index.html not found")
        return

    backup_file(HTML_FILE)

    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace or insert <main>
    html, count = re.subn(r"<main.*?</main>", NEW_MAIN, html, flags=re.S)
    if count == 0:
        print("⚠️ No <main> found, inserting before </body>")
        html = html.replace("</body>", NEW_MAIN + "\n</body>")

    # Replace or insert CSS for .three-columns
    if "main.three-columns" in html:
        html = re.sub(r"main\.three-columns\s*\{.*?\}", CSS_BLOCK, html, flags=re.S)
    else:
        html = html.replace("</style>", CSS_BLOCK + "\n</style>")

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print("✅ index.html patched with 33 | 34 | 33 column layout.")

if __name__ == "__main__":
    patch_index()
