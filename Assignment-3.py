#implement bank  system using classes and objects
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully. Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully. Current Balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")

account1 = BankAccount("Asutosh", 1000)
account2 = BankAccount("nandini", 2000)
account1.deposit(500)
account1.withdraw(300)
account1.check_balance()
account2.deposit(1000)
account2.check_balance()
print("############################################")
#######################################################
#2 question
class Stock:
    def __init__(self, name, symbol, price_per_share, quantity):
        self.name = name
        self.symbol = symbol
        self.price_per_share = price_per_share 
        self.quantity = quantity              

    def buy(self, qty):
        """Buy shares and update total quantity."""
        self.quantity += qty
        total_value = self.quantity * self.price_per_share
        print(f"Bought {qty} shares of {self.name}. Total shares now: {self.quantity}. Total value: Rs.{total_value}")

    def sell(self, qty):
        """Sell shares if enough are available."""
        if qty <= self.quantity:
            self.quantity -= qty
            total_value = self.quantity * self.price_per_share
            print(f"Sold {qty} shares of {self.name}. Remaining shares: {self.quantity}. Total value: Rs.{total_value}")
        else:
            print(f"Not enough shares to sell! You currently own {self.quantity} shares.")

    def __str__(self):
        total_value = self.quantity * self.price_per_share
        return f"{self.name} ({self.symbol}) | Shares: {self.quantity} | Price/Share: Rs.{self.price_per_share} | Total Value: Rs.{total_value}"

tata = Stock("Tata Power", "TATAPOWER", 250, 10)
reliance = Stock("Reliance Industries", "RELIANCE", 500, 5)  

stocks = {"TATAPOWER": tata, "RELIANCE": reliance}

def view_portfolio():
    print("\n--- Your updated Portfolio ---")
    for stock in stocks.values():
        print(stock)

def buy_stock(symbol, qty):
    if symbol in stocks:
        stocks[symbol].buy(qty)
    else:
        print("Stock not found!")

def sell_stock(symbol, qty):
    if symbol in stocks:
        stocks[symbol].sell(qty)
    else:
        print("Stock not found!")
view_portfolio()
buy_stock("TATAPOWER", 10)
buy_stock("RELIANCE", 2)

view_portfolio()
