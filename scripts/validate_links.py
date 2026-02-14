from pathlib import Path
import re


def scan_broken_links() -> int:
    root_dir = Path(__file__).resolve().parent.parent
    guides_dir = root_dir / "_guides"

    valid_slugs = {f.stem for f in guides_dir.glob("*.md")}
    print(f"Indexed {len(valid_slugs)} valid guides.")

    files_to_scan = list(guides_dir.glob("*.md"))
    files_to_scan.append(root_dir / "index.md")
    files_to_scan.append(root_dir / "404.md")
    files_to_scan.append(root_dir / "guides.html")

    link_pattern = re.compile(r"/guides/([a-zA-Z0-9-]+)(?:/|'|\"|\)|})")

    broken_links = []
    print(f"Scanning {len(files_to_scan)} files for broken outgoing links...\n")

    for file_path in files_to_scan:
        if not file_path.exists():
            continue

        content = file_path.read_text(encoding="utf-8", errors="replace")
        for i, line in enumerate(content.splitlines(), start=1):
            for slug in link_pattern.findall(line):
                if slug in {"guides", "assets", "css", "js"}:
                    continue
                if slug not in valid_slugs:
                    broken_links.append((file_path.name, i, slug))

    if not broken_links:
        print("SUCCESS: No broken internal /guides/<slug> links found.")
        return 0

    print(f"FOUND {len(broken_links)} BROKEN LINKS:\n")
    print(f"{'Source File':<40} | {'Line':<5} | {'Invalid Target Slug'}")
    print("-" * 80)
    for source, line, target in broken_links:
        print(f"{source:<40} | {line:<5} | {target}")
    return 1


if __name__ == "__main__":
    raise SystemExit(scan_broken_links())
