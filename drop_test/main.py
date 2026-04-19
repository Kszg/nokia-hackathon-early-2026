from pathlib import Path

def main():
    data = Path(Path(__file__).parent / "input.txt").read_text(encoding="utf-8")
    input_lines = data.splitlines()

    for line in input_lines:
        line_data = line.split(", ")
        print(egg_drop(int(line_data[0]), int(line_data[1])))

def egg_drop(n: int, h: int) -> int:
    max_floors = [0] * (n + 1)
    k = 0

    while (max_floors[n] < h):
        k += 1

        for e in range(n, 0, -1):
            max_floors[e] = max_floors[e] + max_floors[e - 1] + 1
    
    return k

if __name__ == "__main__":
    main()
