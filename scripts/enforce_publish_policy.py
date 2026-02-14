#!/usr/bin/env python3
import pathlib
import sys

from lib.front_matter import parse_front_matter_yaml, split_front_matter


ALLOWED_STATES = {"draft", "verified", "stale-risk", "needs-refresh", "archived"}


def as_bool(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        v = value.strip().lower()
        if v in {"true", "yes", "1", "on"}:
            return True
        if v in {"false", "no", "0", "off"}:
            return False
    return None


def main() -> int:
    guides_dir = pathlib.Path("_guides")
    if not guides_dir.exists():
        print("ERROR: _guides directory not found.")
        return 1

    errors = []
    guide_paths = sorted(guides_dir.glob("*.md"))

    for path in guide_paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        fm_raw, _body, _full = split_front_matter(text)
        if fm_raw is None:
            errors.append(f"{path}: missing front matter.")
            continue

        fm = parse_front_matter_yaml(fm_raw)
        state = str(fm.get("content_state") or "").strip()
        if state not in ALLOWED_STATES:
            errors.append(f"{path}: invalid content_state `{state}`.")
            continue

        published_value = fm.get("published", True)
        published = as_bool(published_value)
        if published is None:
            errors.append(f"{path}: invalid published value `{published_value}`.")
            continue

        if state != "verified" and published:
            errors.append(
                f"{path}: non-verified guide must set `published: false` (content_state={state})."
            )

    if errors:
        print("Publish policy failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"Publish policy passed for {len(guide_paths)} guide(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
