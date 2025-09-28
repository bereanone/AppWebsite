import os

APP_FILE = "src/App.tsx"

def patch_app_file():
    if not os.path.exists(APP_FILE):
        print(f"❌ {APP_FILE} not found")
        return

    with open(APP_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove any old imports of Big.png or Small.png
    for logo in ["Big.png", "Small.png"]:
        if f"import" in content and logo in content:
            print(f"🔄 Removing old import of {logo}")
            content = "\n".join(
                line for line in content.splitlines()
                if logo not in line
            )

    # Replace old <img src="./assets/..."> with public/ references
    content = content.replace(
        'src="./assets/Big.png"',
        'src={`${import.meta.env.BASE_URL}Big.png`}'
    ).replace(
        'src="./assets/Small.png"',
        'src={`${import.meta.env.BASE_URL}Small.png`}'
    )

    # Also handle cases where src="Big.png" was written directly
    content = content.replace(
        'src="Big.png"',
        'src={`${import.meta.env.BASE_URL}Big.png`}'
    ).replace(
        'src="Small.png"',
        'src={`${import.meta.env.BASE_URL}Small.png`}'
    )

    with open(APP_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Patched {APP_FILE} to use public/Big.png and public/Small.png")


def main():
    patch_app_file()
    print("🎉 Done. Now run:")
    print("   rd /s /q dist   # (Windows PowerShell)")
    print("   npm run build")
    print("   git add . && git commit -m 'Fix logo paths' && git push origin main")

if __name__ == "__main__":
    main()
