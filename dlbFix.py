from pathlib import Path
import shutil
from datetime import datetime

ROOT = Path(__file__).parent.resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

# files to scan (recursive) — add more extensions if you like
EXTS = {".html", ".tsx", ".ts", ".css", ".md", ".json"}

def should_edit(path: Path) -> bool:
    return path.suffix.lower() in EXTS and path.is_file()

def replace_all(text: str) -> str:
    # replace any way GoldLogo might be referenced
    reps = {
        'public/GoldLogo.png': 'public/Logo2Small.png',
        '"/GoldLogo.png"': '"public/Logo2Small.png"',
        "'/GoldLogo.png'": "'public/Logo2Small.png'",
        '"GoldLogo.png"': '"public/Logo2Small.png"',
        "'GoldLogo.png'": "'public/Logo2Small.png'",
        '"%BASE_URL%GoldLogo.png"': '"public/Logo2Small.png"',
        # just in case someone used uppercase/lowercase variants
        'GoldLogo.png': 'Logo2Small.png',
    }
    for a, b in reps.items():
        text = text.replace(a, b)
    return text

def main():
    edited = []
    for path in ROOT.rglob("*"):
        if not should_edit(path):
            continue
        original = path.read_text(encoding="utf-8", errors="ignore")
        changed = replace_all(original)
        if changed != original:
            bak = path.with_suffix(path.suffix + f".bak.{STAMP}")
            shutil.copy2(path, bak)
            path.write_text(changed, encoding="utf-8")
            edited.append(path.relative_to(ROOT))

    if not edited:
        print("ℹ No references to GoldLogo.png found.")
    else:
        print("🛠 Updated files:")
        for p in edited:
            print("  -", p)

        print("\n✅ Next:")
        print("   git add -A")
        print('   git commit -m "Force swap GoldLogo → Logo2Small everywhere"')
        print("   git push")
        print("   Then hard-refresh the site (Ctrl+F5).")

if __name__ == "__main__":
    main()
