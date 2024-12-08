"Common test components."

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

TEST_ROOT = Path(__file__).parent

MACRO_RGX = re.compile(r"\{%\s[include].*[-args.md\"]\s%\}")  
MACRO_FILENAME_RGX = re.compile(r"(\w+-args\.md)")  # captures macro file name
KWARGS_REGEX = re.compile(r"\s+(\w+)=\$\{\d+:(.*)\}")  # captures keyword and default value

SNIPPET_FILES = list((TEST_ROOT.parent / "snippets").glob("*.json"))


def clean_macro(m: str) -> re.Match:
    """Extract the file name from a macro string."""
    return re.search(MACRO_FILENAME_RGX, m)


def parse_custom_json(file_path:str | Path) -> dict:
    """Remove comment lines to parse a JSON snippets file and return its content."""
    content = Path(file_path).read_text("utf-8")
    content = re.sub(r'//.*', '', content)  # remove comments
    return json.loads(content)


@dataclass
class Snippet:
    prefix: str
    body: list[str]
    description: str
    name: str = ""
    default_args: dict = field(default_factory=dict)
    
    def __post_init__(self) -> None:
        for line in self.body:
            if "=" in line:
                k,v = getattr(re.search(KWARGS_REGEX, line), "groups", list)()
                self.default_args.update({k:v})
        self.name = self.prefix.replace("ultra.kwargs-", "")
    
    @property
    def get_defaults(self) -> dict:
        return self.default_args

