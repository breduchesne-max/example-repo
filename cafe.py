'''Menu - List with at least four items sold in the café
Stock : Dictionary with stock value for each item on menu
Price : Dictiontionary called price that should contain the prices for each
item on the menu
Calculate the total worth of the stock in the café and then store the results
inside a variable called total stock worth
'''


menu = ['coffee', 'tea', 'sandwich', 'cake']
stock = {'coffee': 10, 'tea': 20, 'sandwich': 15, 'cake': 5}
price = {'coffee': 2.50, 'tea': 1.50, 'sandwich': 3.00, 'cake': 2.00}
total_stock = 0

for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

print("Total stock worth:", total_stock)    