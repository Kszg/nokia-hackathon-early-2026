class BillingManager:
    def __init__(self, total_seconds: int):
        self.unbilled_time = total_seconds
        self.billed_time = 0;
        self.bill = 0
    
    def bill_time(self, total_seconds: int, price: int):
        self.unbilled_time -= total_seconds
        self.billed_time += total_seconds
        self.bill += price
