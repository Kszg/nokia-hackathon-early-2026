from datetime import datetime
from pathlib import Path
from billing_manager import BillingManager

def main():
    # data = Path("input.txt").read_text(encoding="utf-8")
    # print(data, end="")
    print(parking_fee("2026-03-30 00:00:00", "2026-03-30 00:20:00"))
    print(parking_fee("2026-03-30 00:00:00", "2026-03-30 02:00:00"))
    print(parking_fee("2026-03-30 00:00:00", "2026-03-30 04:00:00"))
    print(parking_fee("2026-03-30 00:00:00", "2026-03-31 00:00:00"))

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

if __name__ == "__main__":
    main()
