import json
from pathlib import Path
from typing import LiteralString

'''
Write a python function to parse all the json files found in the snippets directory, and create a markdown formatted table from the "prefix" and "description" keys of each entry. The markdown table should calculate the max space needed for each column based on the contexts of the json file.
'''

class JSONDecoderWithComments(json.JSONDecoder):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.parse_comment = False

    def decode(self, s, *args, **kwargs) -> dict|list|str:
        s = self.strip_comments(s)
        return super().decode(s, *args, **kwargs)
    
    def strip_comments(self, s) -> LiteralString:
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


def parse_json_files(directory):
    table = []
    max_prefix_length = 0
    max_description_length = 0

    # Find all json files in the directory
    json_files = Path(directory).rglob("*.json")

    # Parse each json file
    for file in json_files:
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
directory = r"Q:\ML_dev\ultra_snippets\ultralytics-snippets\snippets"
markdown_table = parse_json_files(directory)
print(markdown_table)
