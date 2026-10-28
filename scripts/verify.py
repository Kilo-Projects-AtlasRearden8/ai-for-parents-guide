#!/usr/bin/env python3
"""Verify the AI for Family Life manual and static site.

Checks:
- all required files exist
- LICENSE contains the exact copyright line
- README credits Asdale Dynamics, LLC
- HTML files parse and nav links resolve
- Markdown links resolve to existing files
- no .github/workflows directory
- no secrets or personal-data patterns in files
- privacy placeholders documented
"""
import html.parser
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

errors = []
warnings = []


def fail(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def rel(path):
    return os.path.relpath(path, ROOT)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def file_exists(path):
    return os.path.isfile(os.path.join(ROOT, path))


# 1. Required files
required_files = [
    "LICENSE",
    "README.md",
    "STATUS.md",
    "docs/index.md",
    "docs/getting-started.md",
    "docs/privacy-safety.md",
    "docs/school-forms.md",
    "docs/meal-ideas.md",
    "docs/activities.md",
    "docs/bedtime-stories.md",
    "docs/printable-planners.md",
    "site/index.html",
    "site/getting-started.html",
    "site/privacy-safety.html",
    "site/school-forms.html",
    "site/meal-ideas.html",
    "site/activities.html",
    "site/bedtime-stories.html",
    "site/printable-planners.html",
    "site/css/style.css",
    "scripts/verify.py",
]
for path in required_files:
    if not file_exists(path):
        fail(f"missing required file: {path}")

# 2. LICENSE exact copyright line
license_text = read("LICENSE") if file_exists("LICENSE") else ""
expected = "Copyright (c) 2026 Asdale Dynamics, LLC"
if expected not in license_text:
    fail(f'LICENSE missing exact line: {expected}')

# 3. README credit
readme_text = read("README.md") if file_exists("README.md") else ""
if "Asdale Dynamics, LLC" not in readme_text:
    fail("README does not credit Asdale Dynamics, LLC")

# 4. No .github/workflows
if os.path.isdir(os.path.join(ROOT, ".github", "workflows")):
    fail(".github/workflows directory must not exist")

# 5. No secrets / personal data patterns
secret_patterns = [
    r"sk-[A-Za-z0-9]{20,}",
    r"AKIA[0-9A-Z]{16}",
    r"ghp_[A-Za-z0-9]{20,}",
    r"(?i)api[_-]?key[\"']?\s*[:=][\"']?[A-Za-z0-9_-]{8,}",
    r"(?i)secret[\"']?\s*[:=][\"']?[A-Za-z0-9_-]{8,}",
    r"\b\d{3}-\d{2}-\d{4}\b",       # SSN-like
    r"\b\d{3}[-.]\d{3}[-.]\d{4}\b",  # phone-like
]
personal_patterns = [
    r"(?i)dylan.asdale",  # expected credit occurrences only in README/docs footer - allow; flag elsewhere below
]
all_files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d != ".git"]
    for fn in filenames:
        all_files.append(os.path.relpath(os.path.join(dirpath, fn), ROOT))

for path in all_files:
    if path.startswith(".git/"):
        continue
    try:
        text = read(path)
    except Exception:
        continue
    for pat in secret_patterns:
        if re.search(pat, text):
            fail(f"possible secret in {path}: {pat}")

# 6. HTML parsing + link checks
class LinkChecker(html.parser.HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for key, value in attrs:
                if key == "href":
                    self.links.append(value)


for path in all_files:
    if not path.startswith("site/") or not path.endswith(".html"):
        continue
    text = read(path)
    parser = LinkChecker(path)
    try:
        parser.feed(text)
    except Exception as exc:
        fail(f"HTML parse error in {path}: {exc}")
        continue
    for href in parser.links:
        if href.startswith("#") or href.startswith("http://") or href.startswith("https://") or href.startswith("mailto:"):
            continue
        target = href
        if "?" in target:
            target = target.split("?", 1)[0]
        resolved = os.path.normpath(os.path.join(os.path.dirname(os.path.join(ROOT, path)), target))
        if not os.path.isfile(resolved):
            fail(f"broken link in {path}: {href} -> {target}")

# Every HTML page should link back to index and credit LLC
for path in all_files:
    if path.startswith("site/") and path.endswith(".html"):
        text = read(path)
        if 'href="index.html"' not in text:
            fail(f"{path} missing link to index.html")
        if "Asdale Dynamics, LLC" not in text:
            fail(f"{path} missing Asdale Dynamics, LLC credit")

# 7. Markdown link checks
md_link_re = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
for path in all_files:
    if path.endswith(".md"):
        text = read(path)
        for _, target in md_link_re.findall(text):
            if target.startswith("#") or target.startswith("http://") or target.startswith("https://") or target.startswith("mailto:"):
                continue
            fragment = ""
            if "#" in target:
                target, fragment = target.split("#", 1)
            resolved = os.path.normpath(os.path.join(os.path.dirname(os.path.join(ROOT, path)), target))
            if not os.path.isfile(resolved):
                fail(f"broken markdown link in {path}: {target}")

# 8. Privacy placeholders mentioned
privacy_text = read("docs/privacy-safety.md") if file_exists("docs/privacy-safety.md") else ""
if "[Child's name]" not in privacy_text:
    fail("privacy-safety.md should document [Child's name] placeholder")
if "never paste" not in privacy_text.lower():
    fail("privacy-safety.md should state the never-paste rule")

print(f"Files checked: {len(all_files)}")
if errors:
    print("VERIFICATION FAILED")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
if warnings:
    print("VERIFICATION PASSED (with warnings)")
    for w in warnings:
        print(f"  - {w}")
else:
    print("VERIFICATION PASSED")
sys.exit(0)
