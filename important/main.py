import requests
import customHashish as hash
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pdfWriter
import gui

# Define the URL for accessing the Shopify store's API
url = 'https://a49ba18159fe5c18878c02cd077c773b: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@lovcompression.myshopify.com/admin/api/2022-04/'

# Function to retrieve orders from the Shopify API

def get_orders():
    endpoint = 'orders.json'
    r = requests.get(url + endpoint)
    return r.json()


class Order:
    orderID = ""
    lineItems = []
    lineItemCount = 0

    def Order(self):
        self.orderID = ""
        self.lineItems = []
        self.lineItemCount = 0

    def setOrderID(self, specificOrderID):
        self.orderID = specificOrderID

    def addLineItem(self, liney):
        self.lineItems.append(liney)
        self.lineItemCount += 1

    def printOrder(self):
        # print(self.orderID)
        print(len(self.lineItems))  # print the line Item at index i
        for item in self.lineItems:
            print(item)


"""|
getSpecificProductID

gets the product ID from a line item

parameters:
    item: the line item - order["line_items"][0]["properties"]

output:
    returns the productID as a string
"""


def getSpecificProductID(item):
    return int(item["product_id"])


# initialize lists
listOfOrders = []  # list of classess
listOfItems = []  # all the line items that have

"""
data search: iterates through the orders and makes a list of class Orders
returns that list
"""


def dataSearch():
    orderData = get_orders()
    i = 0
    for order in orderData["orders"]:
        # creating new instance of order class
        myOrder = Order()
        myOrder.Order()
        myOrder.setOrderID(order["order_number"])

        """
        gathering product ID and customization info
        """
        lineItems = order["line_items"][0]["properties"]
        # converting to float so I can manipulate it if needed

        for i in range(0, len(order["line_items"])):
            myOrder.addLineItem(order["line_items"][i])
            listOfItems.append(order["line_items"][i])

        listOfOrders.append(myOrder)

dataSearch()

def printer():
    for i in len(listOfOrders):
        listOfOrders[i].printOrder()


"""
gets each item's product ID
"""
for item in listOfItems:
    if type(item["product_id"]) == int:
        productID = getSpecificProductID(item)

        hash.getDataFromLineItem(productID, item)

        hash.listOfColorLists["White"]

# pdfWriter.makePDF("White")
gui.mainGui()
# pdfWriter.makePDFs()
# pdfWriter.tester("Black")