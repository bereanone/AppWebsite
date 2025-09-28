import os
import subprocess
import shutil

# --- File paths ---
header_file = "src/components/Header.tsx"
footer_file = "src/components/Footer.tsx"
vite_config = "vite.config.ts"

# --- Patch Header.tsx ---
if os.path.exists(header_file):
    backup = header_file + ".bak"
    shutil.copyfile(header_file, backup)
    with open(header_file, "w", encoding="utf-8") as f:
        f.write("""export default function Header() {
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
""")
    print(f"✅ Patched {header_file}")
else:
    print(f"⚠️ {header_file} not found")

# --- Patch Footer.tsx ---
if os.path.exists(footer_file):
    backup = footer_file + ".bak"
    shutil.copyfile(footer_file, backup)
    with open(footer_file, "w", encoding="utf-8") as f:
        f.write("""export default function Footer() {
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
""")
    print(f"✅ Patched {footer_file}")
else:
    print(f"⚠️ {footer_file} not found")

# --- Patch vite.config.ts ---
if os.path.exists(vite_config):
    backup = vite_config + ".bak"
    shutil.copyfile(vite_config, backup)
    with open(vite_config, "w", encoding="utf-8") as f:
        f.write("""import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  base: "/AppWebsite/",  // 👈 ensures assets load correctly on GitHub Pages
});
""")
    print(f"✅ Patched {vite_config}")
else:
    print(f"⚠️ {vite_config} not found")

# --- Clean dist/ ---
if os.path.exists("dist"):
    shutil.rmtree("dist")
    print("🧹 Removed dist/")

# --- Build ---
print("⚡ Running build...")
try:
    subprocess.run("npm run build", shell=True, check=True)
    print("🎉 Build completed successfully.")
except subprocess.CalledProcessError:
    print("❌ Build failed.")
    exit(1)

# --- Git commit & push ---
print("📦 Committing and pushing to GitHub...")
try:
    subprocess.run("git add .", shell=True, check=True)
    subprocess.run('git commit -m "Fix logos and vite base"', shell=True, check=False)
    subprocess.run("git push origin main", shell=True, check=True)
    subprocess.run("git push origin gh-pages", shell=True, check=True)
    print("🚀 Deploy complete. Site should update shortly.")
except subprocess.CalledProcessError:
    print("⚠️ Git push failed. Please check your repo status.")
