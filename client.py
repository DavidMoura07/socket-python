# Import socket module
import socket
import pickle
from Message.Message import Message
from Message.MessageCodes import MessageCodes
from User.User import User 
from Order.NewOrder import NewOrder

def Authenticate(s, USER, PASS):
    print('Authenticating...')
    auth = User(USER, PASS)
    authMessage = Message(MessageCodes.AUTHENTICATION, auth, True)
    s.send(pickle.dumps(authMessage))
    authResponse = s.recv(4096)
    if (not authResponse):
        print('Server are not responding')
        return
    else:
        responseData = pickle.loads(authResponse)
        print(responseData.data)
        if (responseData.code == MessageCodes.ERROR):
            return
    print()

def GetOrders(s):
    print('- ORDERS')
    getOrderMessage = Message(MessageCodes.GET_ORDERS, '', True)
    s.send(pickle.dumps(getOrderMessage))
    # Receiving list of orders
    orderMessage = pickle.loads(s.recv(4096))
    if orderMessage.code == MessageCodes.ORDERS_LIST:
        for order in orderMessage.data:
            print('- ', order)
        print()

def GetProducts(s):
    print('- PRODUCTS')
    getStockMessage = Message(MessageCodes.GET_PRODUCTS, '', True)
    s.send(pickle.dumps(getStockMessage))
    # Receiving list of products
    stockMessage = pickle.loads(s.recv(4096))
    if stockMessage.code == MessageCodes.PRODUCTS_LIST:
        for item in stockMessage.data:
            print('- ', item)
        print()

def MakeNewOrder(s):
    ans = input('\nDeseja realizar um novo pedido?(y/n): ')
    if ans == 'y':
        while ans == 'y':
            print('\n### SOLICITANDO NOVO ITEM ###')
            product = input('\nQual o nome do produto?\n')
            quantity = input('\nQual a quantidade desejada do produto %s?\n' % (product))
            ans = input('\nDeseja solicitar mais produtos?(y/n): ')
            print('\nValidanto item...')
            newOrder = NewOrder(product, quantity)
            endOfData = False if ans == 'y' else True
            newOrderMessage = Message(MessageCodes.NEW_ORDER_ITEM, newOrder, endOfData)
            s.send(pickle.dumps(newOrderMessage))

            responseData = pickle.loads(s.recv(4096))
            if (responseData.code == MessageCodes.ERROR):
                print('Pedido do item %s não efetuado, motivo:' % (product))
                print(responseData.data)
            else:
                print(responseData.data)
    else:
        return

def Main():
    HOST = '127.0.0.1'
    PORT = 3333

    USER = 'user1'
    PASS = 'senha'

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))

        # Realizando autenticação
        Authenticate(s, USER, PASS)

        # Obtendo lista de pedidos já realizados
        GetOrders(s)

        # Obtendo lista de produtos em estoque
        GetProducts(s)
        
        # realizando novo pedido
        MakeNewOrder(s)

if __name__ == '__main__':
    Main()
