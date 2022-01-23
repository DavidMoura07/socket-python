import csv
from .User import User

def FindAllUsers():
    users = []
    with open('./Data/users.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter = ';')
        for row in reader:
            csvUsers = dict(row)
            user = User(csvUsers['username'], csvUsers['password'])
            users.append(user)
    return users
        
