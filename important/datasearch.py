import requests
import customHash as hash

# Define the URL for accessing the Shopify store's API
url = 'https://6deed5244c09cda4a83b90407bfb70fa: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@lovcompression.myshopify.com/admin/api/2023-07/'


def get_orders(limit, ID):
    # endpoint = f'orders.json?limit=250;created_at_max=2023-10-{date}T23:59:59;status=any'
    endpoint = f'orders.json?limit={limit};since_id={ID};fulfillment_status=unshipped'
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


"""
data search: iterates through the orders and makes a list of class Orders
returns that list
"""


def dataSearch(limit, ID):
    orderData = get_orders(limit, ID)
    for order in orderData["orders"]:
        # creating new instance of order class
        myOrder = Order()
        myOrder.Order()
        myOrder.setOrderID(order["order_number"])

        """
        gathering product ID and customization info
        """
        lineItems = order["line_items"][0]["properties"]

        for i in range(0, len(order["line_items"])):
            myOrder.addLineItem(order["line_items"][i])
            listOfItems.append(order["line_items"][i])

        listOfOrders.append(myOrder)


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
listOfOrders = []  # list of classes
listOfItems = []  # all the line items that have


def printer():
    for i in len(listOfOrders):
        listOfOrders[i].printOrder()


"""
gets each item's product ID
"""


def completeSearch(limit, ID):
    dataSearch(limit, ID)

    for item in listOfItems:
        if type(item["product_id"]) == int:
            productID = getSpecificProductID(item)

            hash.getDataFromLineItem(productID, item)

            hash.colorDataHash["White"]

    print("Finished searching the data")
