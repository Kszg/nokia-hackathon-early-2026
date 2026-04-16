from pathlib import Path

def main():
    data = Path(Path(__file__).parent / "input.txt").read_text(encoding="utf-8")
    input_lines = data.splitlines()
    parsed_lines = []

    for line in input_lines:
        parsed_lines.append(parse_input_line(line))

    print(parsed_lines)

def parse_input_line(input: str) -> str:
    if ("^" in input):
        expression_parts = input.split("^")

        base = int(expression_parts[0])
        exponent = int(expression_parts[1])

        return str(base**exponent)
    
    return input

if __name__ == "__main__":
    main()
