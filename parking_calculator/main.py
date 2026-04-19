from datetime import datetime
from io import TextIOWrapper
from pathlib import Path
from billing_manager import BillingManager

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def main():
    data = Path(Path(__file__).parent / "input.txt").read_text(encoding="utf-8")
    input_lines = data.splitlines()

    bills = []

    for line in input_lines[2:]:
        if (len(line) == 0): continue

        line_data = line.split("\t\t")
        bills.append([line_data[0], int(parking_fee(line_data[1], line_data[2]))])

    print_and_write_to_file(bills, "output.txt")

def parking_fee(start: str, end: str) -> int:
    error = get_error(start, end)
    if (error is not None): raise Exception(error)

    MINUTE = 60
    HOUR = (60*MINUTE)

    HOURLY_RATE = 500
    DAILY_RATE = 10_000
    FREE_PEROID = (30*MINUTE)
    DISCOUNTED_HOURS = 3 # First 3 hours are discounted from 500 to 300.
    DISCOUNT = 200

    bm = BillingManager(timespan_seconds(start, end))

    discounted_hours_remaining = DISCOUNTED_HOURS

    whole_24_hours = bm.unbilled_time // (24*HOUR)
    bm.bill_time(whole_24_hours * (24*HOUR), whole_24_hours * DAILY_RATE)

    bm.bill_time(FREE_PEROID, 0)
    
    while bm.unbilled_time > 0:
        if (discounted_hours_remaining > 0):
            rate = HOURLY_RATE - DISCOUNT
            discounted_hours_remaining -= 1
        else:
            rate = HOURLY_RATE

        bm.bill_time((1*HOUR), rate)
    
    return bm.bill

def get_error(start: str, end: str) -> str:
    try: start_dt = datetime.strptime(start, DATETIME_FORMAT)
    except ValueError: return "Start time does not match format."
    
    try: end_dt = datetime.strptime(end, DATETIME_FORMAT)
    except ValueError: return "End time does not match format."

    if (start_dt >= end_dt): return "End time must be after start."

    return None

def timespan_seconds(start: str, end: str) -> int:
    start_dt = datetime.strptime(start, DATETIME_FORMAT)
    end_dt = datetime.strptime(end, DATETIME_FORMAT)

    return (end_dt - start_dt).total_seconds()

def print_and_write_to_file(bills: list, file_name: str):
    p = Path(Path(__file__).parent / file_name)
    
    with(open(p, "wt", encoding="utf-8") as f):
        write_and_print("RENDSZAM\tDIJ", f)

        for bill in bills:
            write_and_print(f"{bill[0]}\t\t{bill[1]}", f)

def write_and_print(str: str, f: TextIOWrapper):
    f.write(str + "\n")
    print(str)

if __name__ == "__main__":
    main()
