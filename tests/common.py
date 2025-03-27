"Common test components."

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

CHECK = ("kwargs.code-snippets",)

TEST_ROOT = Path(__file__).parent
ROOT = TEST_ROOT.parent.parent  # outside of repo
DOCS_PATH = ROOT / "ultralytics/docs/en"

MACRO_RGX = re.compile(r"\{%\s[include].*[-args.md\"]\s%\}")  
MACRO_FILENAME_RGX = re.compile(r"(\w+-args\.md)")  # captures macro file name
KWARGS_REGEX = re.compile(r"\s+(\w+)=\"?\$\{\d+:?\|?(.*(?<!\|))\|?\}\"?")  # captures keyword and default value or options

ARG_PATH = DOCS_PATH / "macros"
SNIPPET_FILES = list((TEST_ROOT.parent / "snippets").glob("*.code-snippets"))
DOCS_MODE_FILES: list[Path] = list((DOCS_PATH / "modes").glob("*.md"))

SNIP_NUM_ARG = re.compile(r"(\w+=)\$\{\d+:\|?(\d+\.?\d*|\d+\.?\d* or \d+\.?\d*)\|?\}")
SNIP_BOOL_ARG = re.compile(r"(\w+=)\$\{\d+:\|?(True|False)\|?\}")
SNIP_OPTIONS_ARG = re.compile(r'(\w+=)\\?\"?\$\{\d+\|(.*(?<!\|))\|\}\\?\"?')  # captures "arg=" and | {OPTIONS} |
SNIP_NONE_ARG = re.compile(r"(\w+=)\$\{\d+:\|?None\|?\}")

ALT_DEFAULTS = {  # acceptable alternate default values
    "data": "coco8.yaml",
    "source": "",
}

def clean_macro(m: str) -> re.Match:
    """Extract the file name from a macro string."""
    return re.search(MACRO_FILENAME_RGX, m)


def parse_custom_json(file_path:str | Path) -> dict:
    """Remove comment lines to parse a JSON snippets file and return its content."""
    content = Path(file_path).read_text("utf-8")
    content = re.sub(r'//.*', '', content)  # remove comments
    return json.loads(content)


def str2num(s: str) -> float | int:
    """Convert a string to a number, removes grave character."""
    s = s.strip('`')
    return float(s) if '.' in s else int(s)


def default_is_none(d: dict) -> bool:
    """Check if the default value is None."""
    return d.get("Default", None) == "`None`"


def first_type(d: dict) -> str:
    """Return the first type in a string."""
    return str(str(d.get("Type", "str")).split(" or ")[0])


def num_args(l: list[str]) -> dict:
    """Return the number of arguments in a list."""
    return {k.strip("").replace("=", ""): str2num(v) for k,v in re.findall(SNIP_NUM_ARG, "\n".join(l))}


def bool_args(l: list[str]) -> dict:
    """Return the boolean arguments in a list."""
    return {k.strip("").replace("=", ""): bool(v) for k,v in re.findall(SNIP_BOOL_ARG, "\n".join(l))}


def options_args(l: list[str]) -> dict:
    """Return the options arguments in a list."""
    return {k.strip("").replace("=", ""): v.split(",") for k,v in re.findall(SNIP_OPTIONS_ARG, "\n".join(l))}


def none_args(l: list[str]) -> dict:
    """Return the None arguments in a list."""
    return {k.strip("").replace("=", ""): None for k in re.findall(SNIP_NONE_ARG, "\n".join(l))}


@dataclass
class Snippet:
    """
    Snippet class to represent a code snippet with metadata.

    Attributes:
    ---
    prefix (str):
        The prefix of the snippet.
    body (list[str]):
        The body of the snippet as a list of strings.
    description (str):
        A description of the snippet.
    name (str):
        The name of the snippet. Defaults to an empty string.
    default_args (dict):
        A dictionary of default arguments. Defaults to an empty dictionary.
    
    Methods:
    ---
    __post_init__() -> None:
        Processes the body of the snippet to extract default arguments and updates the name attribute.
    get_defaults() -> dict:
        Returns the default arguments of the snippet.
    """
    prefix: str
    body: list[str]
    description: str
    name: str = ""
    default_args: dict = field(default_factory=dict)
    
    def __post_init__(self) -> None:
        for line in self.body:
            if "=" in line:
                k,v = getattr(re.search(KWARGS_REGEX, line), "groups", list)()
                if "," in v:
                    v = v.split(",")[0]
                    # TODO: also keep track of available options
                self.default_args.update({k:v})
        self.name = self.prefix.replace("ultra.kwargs-", "")
    
    @property
    def defaults(self) -> dict:
        return self.default_args


@dataclass
class Args:
    """
    A class to represent command-line arguments with additional metadata.
    
    Attributes:
    ---
    argument : str
        The name of the argument.
    default : str
        The default value of the argument.
    description : str
        A description of the argument.
    type : str, optional
        The type of the argument (default is an empty string).
    range : str, optional
        The range of acceptable values for the argument (default is an empty string).
    min : str, optional
        The minimum value in the range (default is an empty string).
    max : str, optional
        The maximum value in the range (default is an empty string).
    
    Methods:
    ---
    __post_init__() -> None:
        Processes the range attribute to convert it into a tuple of numeric values and sets the min and max attributes accordingly.
    """
    argument: str
    default: str
    description: str
    type: str = ""
    range: str = ""
    min: str = ""
    max: str = ""

    def __post_init__(self) -> None:
        if self.range and self.range != "-":
            splitter = " or " if " or " in self.range else " - "
            self.range = tuple((str2num(n.strip().strip("><=")) for n in self.range.split(splitter)))
        self.min = min(self.range) if self.range else "NaN"
        self.max = max(self.range) if self.range else "NaN"
        self.description = "".join(self.description.strip().split("\n"))
    
    def asdict(self) -> dict:
        """Return the object as a dictionary."""
        return {
            "Argument": self.argument,
            "Default": self.default,
            "Description": self.description,
            "Type": self.type,
            "Range": self.range,
            "Min": self.min,
            "Max": self.max
        }


@dataclass
class DocArgs:
    """
    A class to represent document arguments.

    Attributes:
    ---
    name : str
        The name of the document.
    mode : str
        The mode of the document.
    arg_dict : list[dict]
        A list of dictionaries containing argument details.
    
    Methods:
    ---
    __post_init__() -> None:
        Initializes the arguments and sets attributes based on the argument dictionary.
    asdict() -> dict:
        Returns the object as a dictionary.
    """
    name: str
    mode: str
    arg_dict: list[dict]
    
    def __post_init__(self) -> None:
        self.args: list[Args] = [Args(**{str(k).lower():v for k,v in a.items()}) for a in self.arg_dict]
        _ = [setattr(self, a.argument, a.default) for a in self.args]
    
    def asdict(self) -> dict:
        """Return the object as a dictionary."""
        return {"Name": self.name, "Mode": self.mode, "Args": [a.asdict() for a in self.args]}

    @property
    def defaults(self) -> dict[str, str]:
        """Return the default arguments."""
        return {a.argument: a.default for a in self.args}


# Match macros for args to their respective mode files
modes = {k.stem:[] for k in DOCS_MODE_FILES}
for doc in DOCS_MODE_FILES:
    content = doc.read_text("utf-8")
    macros = re.findall(MACRO_RGX, content)
    for macro in macros:
        macro_file = getattr(clean_macro(macro), "group", lambda: None)()
        modes[doc.stem].append(macro_file) if macro_file else None

ARGS_DOCS: list[Path] = [ARG_PATH / file for _,v in modes.items() for file in v]

def make_snippet_and_kwarg_files():
    # Parse the args from docs and macros
    all_args = {m: [] for m in modes}
    for doc in ARGS_DOCS:
        doc_args = []
        lines = doc.read_text("utf-8").split("\n")
        headers = [h.strip() for h in lines.pop(0).split("|") if h.strip() != "" and h != ""]
        
        for i, line in enumerate(lines[1:]):
            if not line.strip():
                continue
            values = (e.strip().strip("`") for e in line.split("|") if e.strip() != "" and e != "")
            doc_args.append(dict(zip(headers, values)))
        
        mode = [k for k,v in modes.items() if doc.name in v][0]
        all_args[mode] += [DocArgs(doc.stem, mode, doc_args)]  # NOTE since making DocArgs object, will have multiple entries


    snippets = []
    for snippet in SNIPPET_FILES:
        if snippet.name in CHECK:
            j_snip: dict[str, dict | str] = parse_custom_json(snippet)
            for n,e in j_snip.items():
                this_snippet = Snippet(
                    prefix=e.get('prefix', ""),
                    body=e.get('body', ["",]),
                    description=e.get('description', "")
                )
                snippets.append(this_snippet)

    _ = Path("all_args.code-snippets").write_text(
        json.dumps({k:[arg.asdict() for arg in args if arg] for k,args in all_args.items()}, indent=4),
        "utf-8"
    )
    _ = Path("snippets.code-snippets").write_text(
            json.dumps({snippet.name: snippet.__dict__ for snippet in snippets}, indent=4),
            "utf-8"
        )


if __name__ == "__main__":
    make_snippet_and_kwarg_files()

    from pprint import pprint as pp
    
    snippets = json.loads(Path("snippets.code-snippets").read_text("utf-8"))
    all_args = json.loads(Path("all_args.code-snippets").read_text("utf-8"))
    
    for snippet in snippets:
        pp(snippet.get_defaults)
        pp(snippet.name)
        pp(snippet.description)
        pp(snippet.body)
    pp(all_args)



# TODO: use snippets and all_args to generate tests