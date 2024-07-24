import json
from pathlib import Path
from typing import LiteralString

class JSONDecoderWithComments(json.JSONDecoder):
    """
    A custom JSON decoder that removes comments from the input string before decoding.

    This class extends the `json.JSONDecoder` class and overrides the `decode` method to remove comments
    from the input string before decoding it into a Python object.

    Attributes:
        parse_comment (bool): Flag indicating whether to parse comments or not.

    Methods:
        decode(s, *args, **kwargs): Decodes the input string after removing comments.
        strip_comments(s): Removes comments from the input string.
    """
    
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.parse_comment = False
    
    
    def decode(self, s, *args, **kwargs) -> dict|list|str:
        """
        Decodes the input string after removing comments.

        Args:
            s (str): The input string to decode.
            *args: Additional arguments to pass to the `json.JSONDecoder.decode` method.
            **kwargs: Additional keyword arguments to pass to the `json.JSONDecoder.decode` method.

        Returns:
            dict|list|str: The decoded Python object.
        """
        s = self.strip_comments(s)
        return super().decode(s, *args, **kwargs)
    

    def strip_comments(self, s) -> LiteralString:
        """
        Removes comments from the input string.

        Args:
            s (str): The input string to remove comments from.

        Returns:
            LiteralString: The input string with comments removed.
        """
        lines = s.split("\n")
        stripped_lines = []
        for line in lines:
            if self.parse_comment:
                if line.strip().endswith("*/"):
                    self.parse_comment = False
            elif line.strip().startswith("//"):
                continue
            elif line.strip().startswith("/*"):
                self.parse_comment = True
            else:
                stripped_lines.append(line)
        return "\n".join(stripped_lines)


def parse_json_files(directory:str|Path) -> LiteralString | str:
    """
    Parses all JSON files in the specified directory and generates a markdown table.

    Args:
        directory (str or Path): The directory path containing the JSON files.

    Returns:
        LiteralString or str: The generated markdown table.
    """

    table = []
    max_prefix_length = 0
    max_description_length = 0

    # Find all json files in the directory
    json_files = Path(directory).rglob("*.json")

    # Parse each json file
    for file in json_files:
        print(f"Reading {file}")
        with open(file) as f:
            data = json.load(f, cls=JSONDecoderWithComments)

        # Iterate over each entry in the json file
        for title, d in data.items():
            prefix = d.get("prefix", "")
            description = d.get("description", "")

            # Update max length for prefix and description
            max_prefix_length = max(max_prefix_length, len(prefix))
            max_description_length = max(max_description_length, len(description))

            # Append entry to the table
            table.append((prefix, description))

    # Generate the markdown table
    markdown_table = f"| {'Prefix'.ljust(max_prefix_length)} | {'Description'.ljust(max_description_length)} |\n"
    markdown_table += f"| {'-' * max_prefix_length} | {'-' * max_description_length} |\n"
    for entry in table:
        prefix = entry[0]
        description = entry[1]
        markdown_table += f"| {prefix.ljust(max_prefix_length)} | {description.ljust(max_description_length)} |\n"

    return markdown_table

# Example usage
directory = Path.cwd() / "ultralytics-snippets/snippets"
markdown_table = parse_json_files(directory)
print(markdown_table)
