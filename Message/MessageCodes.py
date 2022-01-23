from enum import Enum

class MessageCodes(Enum):
    AUTHENTICATION = 1
    GET_PRODUCTS = 2
    PRODUCTS_LIST = 3
    GET_ORDERS = 4
    ORDERS_LIST = 5
    NEW_ORDER_ITEM = 6
    SUCCESS = 7
    ERROR = 8