from pathlib import Path

from src.models.adapter import Adapter
from src.models.parsed_file import ParsedFile
from src.ipconfig_reader import IpConfigReader
from src.io_util import IOUtil

def main():
    input_files = IOUtil.get_input_files(Path(__file__).parent)
    parsed_files = []

    for f in input_files:
        parsed_files.append(ParsedFile(f.name,IpConfigReader.get_adapters(
            f.read_text(encoding="utf-16").splitlines())).__dict__
        )
    
    IOUtil.print_and_write_to_file(parsed_files, Path(Path(__file__).parent / "adapters.json"))

if __name__ == "__main__":
    main()
