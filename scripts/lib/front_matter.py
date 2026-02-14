import re
from typing import Any


_FRONT_MATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", flags=re.DOTALL)


def split_front_matter(text: str):
    match = _FRONT_MATTER_RE.match(text)
    if not match:
        return None, "", text
    return match.group(1), text[match.end() :], text


def parse_front_matter_yaml(yaml_text: str) -> dict[str, Any]:
    try:
        import yaml  # type: ignore
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "Missing dependency: pyyaml. Install with `python -m pip install pyyaml`."
        ) from exc

    data = yaml.safe_load(yaml_text) if yaml_text else None
    if data is None:
        return {}
    if not isinstance(data, dict):
        return {}
    return data

