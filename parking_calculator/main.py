from datetime import datetime
from io import TextIOWrapper
from pathlib import Path
from billing_manager import BillingManager

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
    MINUTE = 60
    HOUR = (60*MINUTE)

    HOURLY_RATE = 500
    DAILY_RATE = 10_000
    FREE_PEROID = (30*MINUTE)
    DISCOUNTED_HOURS = 3 # First 3 hours are discounted from 500 to 300.
    DISCOUNT = 200

    bm = BillingManager(timespan_seconds(start, end))

    discounted_hours_remaining = DISCOUNTED_HOURS

    if (bm.unbilled_time < (24*HOUR)):
        # 24 hours is billed for a fixed fare, so the first 30 minutes shouldn't be free.
        bm.bill_time(FREE_PEROID, 0)
    else:
        whole_24_hours = bm.unbilled_time // (24*HOUR)
        bm.bill_time(whole_24_hours * (24*HOUR), whole_24_hours * DAILY_RATE)

        discounted_hours_remaining -= (whole_24_hours*24*HOUR)
    
    while bm.unbilled_time > 0:
        if (discounted_hours_remaining > 0):
            rate = HOURLY_RATE - DISCOUNT
            discounted_hours_remaining -= 1
        else:
            rate = HOURLY_RATE

        bm.bill_time((1*HOUR), rate)
    
    return bm.bill

def timespan_seconds(start: str, end: str) -> int:
    FORMAT = "%Y-%m-%d %H:%M:%S"

    start_dt = datetime.strptime(start, FORMAT)
    end_dt = datetime.strptime(end, FORMAT)

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
