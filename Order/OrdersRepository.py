import csv
from .Order import Order

def FindAllOrders():
    orders = []
    with open('./Data/orders.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter = ';')
        for row in reader:
            csvOrders = dict(row)
            order = Order(csvOrders['customer'], csvOrders['product'], csvOrders['price'], csvOrders['quantity'], csvOrders['datetime'])
            orders.append(order)
    return orders

def CreateNewOrder(user, product):
    orders = []
    with open('./Data/orders.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter = ';')
        for row in reader:
            csvOrders = dict(row)
            order = Order(csvOrders['customer'], csvOrders['product'], csvOrders['price'], csvOrders['quantity'], csvOrders['datetime'])
            orders.append(order)
    return orders
        
