import csv
from .Product import Product

def FindAllProducts():
    products = []
    with open('./Data/products.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter = ';')
        for row in reader:
            csvProduct = dict(row)
            product = Product(csvProduct['name'], float(csvProduct['price']), int(csvProduct['stock_quantity']))
            products.append(product)
    return products
        
