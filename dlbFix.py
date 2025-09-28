import os
import shutil
import subprocess

header_file = "src/components/Header.tsx"
footer_file = "src/components/Footer.tsx"

# --- Patch Helper ---
def patch_file(filepath, new_content):
    if not os.path.exists(filepath):
        print(f"⚠️ File not found: {filepath}")
        return

    backup_path = filepath + ".bak"
    shutil.copy(filepath, backup_path)
    print(f"📂 Backup created at {backup_path}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ Patched {filepath}")

# --- New Content ---
header_content = """export default function Header() {
  return (
    <header className="header">
      <img
        src={`${import.meta.env.BASE_URL}Big.png`}
        alt="Biblical Heritage Logo"
        className="logo"
      />
    </header>
  );
}
"""

footer_content = """export default function Footer() {
  return (
    <footer className="footer">
      <img
        src={`${import.meta.env.BASE_URL}Small.png`}
        alt="Biblical Heritage Logo Small"
        className="logo"
      />
      <p>© 2025 Biblical Heritage. All rights reserved. | email: OurBiblicalHeritage@gmail.com</p>
    </footer>
  );
}
"""

print("📂 Forcing Header → Big.png (via BASE_URL), Footer → Small.png (via BASE_URL)...")
patch_file(header_file, header_content)
patch_file(footer_file, footer_content)

# --- Clean build folder ---
print("🧹 Cleaning dist folder...")
if os.path.exists("dist"):
    shutil.rmtree("dist")
    print("   Removed dist/")

# --- Build ---
print("⚡ Running build...")
try:
    subprocess.run("npm run build", shell=True, check=True)
    print("🎉 Build completed successfully.")
except subprocess.CalledProcessError:
    print("❌ Build failed. Exiting.")
    exit(1)

# --- Git commit and push ---
print("📦 Committing and pushing to gh-pages...")
try:
    subprocess.run("git add .", shell=True, check=True)
    subprocess.run('git commit -m "Fix: Header→Big.png, Footer→Small.png via BASE_URL"', shell=True, check=False)
    subprocess.run("git push origin main", shell=True, check=True)
    subprocess.run("git push origin gh-pages", shell=True, check=True)
    print("🚀 Deploy complete. Site should update shortly.")
except subprocess.CalledProcessError:
    print("⚠️ Git push failed. Please check your repo status.")
