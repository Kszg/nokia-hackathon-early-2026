from pathlib import Path

def main():
    data = Path(Path(__file__).parent / "input.txt").read_text(encoding="utf-8")
    input_lines = data.splitlines()

    for line in input_lines:
        print(next_palindrome(parse_input_line(line)))

def parse_input_line(input: str) -> str:
    if ("^" in input):
        expression_parts = input.split("^")

        base = int(expression_parts[0])
        exponent = int(expression_parts[1])

        return str(base**exponent)
    
    return input

def next_palindrome(input: str) -> str:
    middle_index = len(input)//2
    odd_length = len(input)%2 != 0

    first_half = input[0:middle_index]
    middle_char = input[middle_index:len(input)-middle_index] # Empty in case of even-length input

    palindrome = first_half + middle_char + first_half[::-1]

    if (int(palindrome) > int(input)): return palindrome

    start = str(int(first_half + middle_char) + 1)

    length_increased = len(start) > len(first_half) + len(middle_char)
    if (length_increased): return "1" + (len(input)-1)*"0" + "1"

    first_half = start[0:-1] if odd_length else start
    middle_char = start[-1] if odd_length else ""

    return first_half + middle_char + first_half[::-1]

if __name__ == "__main__":
    main()
