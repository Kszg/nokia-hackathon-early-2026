from pathlib import Path

def main():
    data = Path(Path(__file__).parent / "input.txt").read_text(encoding="utf-8")
    input_lines = data.splitlines()
    parsed_lines = []

    for line in input_lines:
        parsed_lines.append(parse_input_line(line))

    for line in parsed_lines:
        if (len(line) % 2 == 0):
            print(f"{line}: {next_palindrome(line)}")

def parse_input_line(input: str) -> str:
    if ("^" in input):
        expression_parts = input.split("^")

        base = int(expression_parts[0])
        exponent = int(expression_parts[1])

        return str(base**exponent)
    
    return input

def next_palindrome(input: str) -> str:
    first_half = input[:len(input) // 2]
    palindrome = first_half + first_half[::-1]
    
    if (int(palindrome) > int(input)): return palindrome

    first_half = str(int(first_half) + 1)

    return first_half + first_half[::-1]

if __name__ == "__main__":
    main()
