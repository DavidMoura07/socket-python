import socket
import pickle
from _thread import *
import threading
from Product.ProductsRepository import FindAllProducts, UpdateProduct
from User.UsersRepository import FindAllUsers
from Order.OrdersRepository import FindAllOrders, CreateNewOrder
from Order.NewOrder import NewOrder
from Message.MessageCodes import MessageCodes
from Message.Message import Message
from User.User import User 

print_lock = threading.Lock()

# Função que será usada pelas threads para tratar as requisições dos clientes
def threaded(c, users):

    loggedUser = User('','')
    data = c.recv(4096) # 4096 é o tamanho max de dados que aceita receber
    if not data:
        print('Closing connection')
        return
    else:
        receivedMessage = pickle.loads(data)
        if (receivedMessage.code == MessageCodes.AUTHENTICATION):
            user = next((x for x in users if x.username == receivedMessage.data.username and x.password == receivedMessage.data.password), None)
            if (not user):
                authMessage = Message(MessageCodes.ERROR, "Unauthorized.", True)
                c.send(pickle.dumps(authMessage))
                print('Invalid credentials, closing connection')
                return
            else:
                authMessage = Message(MessageCodes.SUCCESS, "Authenticated.", True)
                c.send(pickle.dumps(authMessage))
                loggedUser = user
                print("Authenticated.")
        else:
            authMessage = Message(MessageCodes.ERROR, "Auth is required.", True)
            c.send(pickle.dumps(authMessage))
            print('Auth is required, closing connection')
            return

    while True:
        data = c.recv(4096)
        if not data:
            print('Closing connection')
            return
        else:
            receivedMessage = pickle.loads(data)

            # GET_ORDERS
            if (receivedMessage.code == MessageCodes.GET_ORDERS):
                orders = FindAllOrders()
                userOrders = [x for x in orders if x.customer == loggedUser.username]
                orderMessage = Message(MessageCodes.ORDERS_LIST, userOrders, True)
                c.send(pickle.dumps(orderMessage))

            # GET_STOCK
            elif (receivedMessage.code == MessageCodes.GET_PRODUCTS):
                products = FindAllProducts()
                productsInStock = [x for x in products if x.stockQuantity > 0]
                productsMessage = Message(MessageCodes.PRODUCTS_LIST, productsInStock, True)
                c.send(pickle.dumps(productsMessage))

            # NEW_ORDER
            elif (receivedMessage.code == MessageCodes.NEW_ORDER_ITEM):
                print_lock.acquire() # ativa a trava para garantir o estado atual do estoque
                
                item = receivedMessage.data
                products = FindAllProducts()
                productRequired = next((x for x in products if x.name == item.productName), None)
                if (not productRequired):
                    responseMessage = Message(MessageCodes.ERROR, 'Produto %s não encontrado' % (item.productName), True)
                    c.send(pickle.dumps(responseMessage))
                else:
                    if (item.quantity > productRequired.stockQuantity):
                        responseMessage = Message(MessageCodes.ERROR, 'Quantidade em estoque insuficiente. Solicitado %s, disponível %s' % (item.quantity, productRequired.stockQuantity), True)
                        c.send(pickle.dumps(responseMessage))
                    else:
                        responseMessage = Message(MessageCodes.SUCCESS, 'Pedido registrado com sucesso.', True)
                        CreateNewOrder(loggedUser, productRequired, item.quantity)
                        productRequired.DecreaseStock(item.quantity)
                        UpdateProduct(productRequired)
                        c.send(pickle.dumps(responseMessage))
                print_lock.release() # libera a trava nas threads
                


def Main():
    HOST = '127.0.0.1'
    PORT = 3333

    threads = []

    # carregando lista de usuários na memória
    users = FindAllUsers()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print("socket binded to port", PORT)
        s.listen(100)
        print("socket is listening")

        while True:
            conn, addr = s.accept() # estabelece conexão com o cliente 
            print('Connected to: ', addr[0], ':', addr[1])
            start_new_thread(threaded, (conn, users)) # cria uma nova thread e retorna seu id

if __name__ == '__main__':
    Main()
