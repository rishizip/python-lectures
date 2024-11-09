# create a class called Order which stores item & its price
# use dunder function __gt__() to convey that
# order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        return self.price > other.price

# Get user input for two orders
item1 = input("Enter item name for order 1: ")
price1 = float(input("Enter price for order 1: "))

item2 = input("Enter item name for order 2: ")
price2 = float(input("Enter price for order 2: "))

# Create Order objects
order1 = Order(item1, price1)
order2 = Order(item2, price2)

# Compare the orders and print the result
if order1 > order2:
    print(f"Order 1 ({order1.item}) is more expensive.")
elif order1.price == order2.price:
    print(f"Both orders are the same price.")
else:
    print(f"Order 2 ({order2.item}) is more expensive.")
