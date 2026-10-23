"""Build the approved static website without including development files."""
from pathlib import Path
import shutil
root = Path(__file__).resolve().parents[1]
out = root / "_site"
if out.exists():
    shutil.rmtree(out)
out.mkdir()
files = ["index.html", "brhc.html", "studybible.html", "downloads.html",
         "privacy.html", "usermanual.html", "listening.html", "preview.css",
         "Big.png", "Small.png", "image.png", "brhc_1914_cover.jpg",
         "listening-center-v1.png", "CNAME"]
for name in files:
    shutil.copy2(root / name, out / name)
for name in ["support", "manual_images"]:
    shutil.copytree(root / name, out / name)
(out / ".nojekyll").touch()
print("Prepared static website in", out)
