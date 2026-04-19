import json
import re
from pathlib import Path
from .models.parsed_file import ParsedFile

class IOUtil:
    @staticmethod
    def get_input_files(dir: Path) -> list[str]:
        pattern = re.compile(r"parser_input_[a-z]\.txt$")

        files = sorted(
            [f for f in dir.iterdir() if f.is_file() and pattern.match(f.name)],
            key=lambda f: f.name
        )

        return files

    @staticmethod
    def print_and_write_to_file(parsed_files: list[ParsedFile], path: Path):
        json_string = json.dumps(parsed_files, indent=2)

        with(open(path, "wt", encoding="utf-8") as f):
            f.write(json_string)

        print(json_string)
