import csv
from .Order import Order
from datetime import datetime

def FindAllOrders():
    orders = []
    with open('./Data/orders.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter = ';')
        for row in reader:
            csvOrders = dict(row)
            order = Order(csvOrders['customer'], csvOrders['product'], csvOrders['price'], csvOrders['quantity'], csvOrders['datetime'])
            orders.append(order)
    return orders

def CreateNewOrder(user, product, quantity):
    headersCSV = ['customer', 'product', 'price', 'quantity', 'datetime'] 
    order = Order(user.username, product.name, product.price, quantity, datetime.now())
    with open('./Data/orders.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headersCSV, delimiter = ';')
        writer.writerow(vars(order))
        file.close()
