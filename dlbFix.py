import re
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
TS = datetime.now().strftime("%Y-%m-%d-%H%M%S")

HTML_FILES = [ROOT / "index.html"]
TSX_FILES = [
    ROOT / "src" / "components" / "Header.tsx",
    ROOT / "src" / "components" / "Footer.tsx",
    ROOT / "src" / "App.tsx",
    ROOT / "src" / "pages" / "PrivacyPage.tsx",
    ROOT / "src" / "components" / "SecondaryLayout.tsx",
]

# Add filenames here if you introduce more public assets later
IMG_NAMES = ["GoldLogo.png", "Logo2.png", "Logo2Small.png", "vite.svg", "react.svg"]
IMG_ALT = "(" + "|".join(map(re.escape, IMG_NAMES)) + ")"

EMAIL_NEW = "OurBiblicalHeritage@gmail.com"

def backup(path: Path):
    if path.exists():
        bak = path.with_suffix(path.suffix + f".bak.{TS}")
        shutil.copy2(path, bak)
        print(f"📦 Backup -> {bak}")
    else:
        print(f"↪ Skipped (not found): {path}")

def patch_index_html(path: Path):
    if not path.exists():
        return
    backup(path)
    text = path.read_text(encoding="utf-8")

    # src="/Logo.png" or src="Logo.png"  ->  src="%BASE_URL%Logo.png"
    attr_pat = re.compile(r'src\s*=\s*"(?:/)?(?P<file>' + IMG_ALT + r')"', re.IGNORECASE)
    text = attr_pat.sub(lambda m: 'src="%BASE_URL%{}"'.format(m.group("file")), text)

    # Update mailto + visible email text lines like: email: someone@domain
    text = re.sub(r'href\s*=\s*"mailto:[^"]+"', 'href="mailto:{}"'.format(EMAIL_NEW), text, flags=re.IGNORECASE)
    text = re.sub(r'email:\s*[^<\s]+@[^<\s]+', 'email: {}'.format(EMAIL_NEW), text, flags=re.IGNORECASE)

    path.write_text(text, encoding="utf-8")
    print(f"🛠 Patched {path.relative_to(ROOT)}")

def patch_tsx_file(path: Path):
    if not path.exists():
        return
    backup(path)
    text = path.read_text(encoding="utf-8")

    # Desired JSX form: src={`${import.meta.env.BASE_URL}FILENAME`}
    def jsx_src(filename: str) -> str:
        return 'src={`${{import.meta.env.BASE_URL}}' + filename + '`}'

    # Case 1: src="Logo.png" or src="/Logo.png"
    attr_pat = re.compile(r'src\s*=\s*"(?:/)?(?P<file>' + IMG_ALT + r')"', re.IGNORECASE)
    text = attr_pat.sub(lambda m: jsx_src(m.group("file")), text)

    # Case 2: src={'/Logo.png'} or src={"Logo.png"}
    braced_pat = re.compile(r'src\s*=\s*\{\s*["\']/?(?P<file>' + IMG_ALT + r')["\']\s*\}', re.IGNORECASE)
    text = braced_pat.sub(lambda m: jsx_src(m.group("file")), text)

    # Update any mailto + visible email addresses
    text = re.sub(r'href\s*=\s*{"?mailto:[^"}]+("?)}?', 'href="mailto:{}"'.format(EMAIL_NEW), text, flags=re.IGNORECASE)
    text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', EMAIL_NEW, text)

    path.write_text(text, encoding="utf-8")
    print(f"🛠 Patched {path.relative_to(ROOT)}")

def main():
    print("=== dlbFix: Pages-safe asset paths + footer email ===")
    for p in HTML_FILES:
        patch_index_html(p)
    for p in TSX_FILES:
        patch_tsx_file(p)

    print("\n✅ Done. Next run:")
    print('   git add .')
    print('   git commit -m "Fix: base-aware image paths + footer email"')
    print('   git push')

if __name__ == "__main__":
    main()
