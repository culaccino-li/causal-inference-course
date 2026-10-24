# Validate the relative lesson paths before publication.
from pathlib import Path
import re, sys
root = Path(__file__).resolve().parent
index = (root / 'index.html').read_text(encoding='utf-8')
paths = sorted(set(re.findall(r'"filename":"(lessons/[^" ]+\.html)"', index)))
missing = [p for p in paths if not (root / p).exists()]
print(f"Found {len(paths)} linked lesson files")
if missing:
    print('Missing:', missing)
    sys.exit(1)
if len(paths) != 14:
    print('Expected 14 modules')
    sys.exit(1)
print('OK: all 14 files exist')
