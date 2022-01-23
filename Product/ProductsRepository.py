import csv
from .Product import Product
from tempfile import NamedTemporaryFile
import shutil

FILENAME = './Data/products.csv'

def FindAllProducts():
    products = []
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file, delimiter = ';')
        for row in reader:
            csvProduct = dict(row)
            product = Product(csvProduct['name'], float(csvProduct['price']), int(csvProduct['stock_quantity']))
            products.append(product)
    return products
        
def UpdateProduct(product):
    tempfile = NamedTemporaryFile(mode='w', delete=False)

    fields = ['name', 'price', 'stock_quantity']

    with open(FILENAME, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields, delimiter = ';')
        writer = csv.DictWriter(tempfile, fieldnames=fields, delimiter = ';')
        for row in reader:
            if row['name'] == product.name:
                row['name'], row['price'], row['stock_quantity'] = product.name, product.price, product.stockQuantity
            row = {'name': row['name'], 'price': row['price'], 'stock_quantity': row['stock_quantity']}
            writer.writerow(row)
    shutil.move(tempfile.name, FILENAME)