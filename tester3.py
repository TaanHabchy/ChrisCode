import datetime
import requests
import colorSort as cs
import numpy as np
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Define the URL for accessing the Shopify store's API
url = 'https://7e9f940f3dbb4372bc2c756d2617ab8d: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@lovcompression.myshopify.com/admin/api/2022-04/'

# Initialize an empty list to store order information
prodIDs = [] # list of the product ID right when read
productCustoms = {} # hashmap of the product ID and the order customizations
IDproducts = [] # all the product IDs, including the manipulated ones
IDNumbers = [] # ID numbers
orderNumbers= [] # list of order numbers

# Function to retrieve orders from the Shopify API
def get_orders():
    endpoint = 'orders.json'
    r = requests.get(url + endpoint)
    return r.json()

# Function to search for orders, extract customization information, and create MyOrder instances
def orderSearch():
    orders = get_orders()
    namer = 0.1 # used to keep the product ID numbers unique for the hashmap

    if 'orders' in orders:

        for order in orders['orders']: # going through the different orders
            IDNumbers.append(order["id"]) # adding ID numbers to list
            orderNumbers.append(order["order_number"]) # ""

            # Extract customization information from line items
            lineItems = order["line_items"][0]["properties"] # gathering product ID and customization info
            productID = float(order["line_items"][0]["product_id"]) # converting to float so I can manipulate it if needed
            # print(type(productID))

            if productID not in prodIDs: # if its a new product ID
                prodIDs.append(productID) 
                productCustoms[productID] = {} # creating a hashmap instance in the productCustoms instance
                IDproducts.append(productID) 
            
            else: 
                prodIDs.append(productID) #pretty sure this aint necessary
                IDproducts.append(productID + namer) # adding a decimal to the end so it is unique in the hashmap productCustoms
                productID = productID + namer # update productID so it unique in hashmap
                productCustoms[productID] = {} # create hashmap instance
                namer += 0.1 

            for i in range(0, len(prodIDs)): # convert all product ID to floats so they can be read in IDValue
                prodIDs[i] = float(prodIDs[i])
            
            for i in range(0, len(lineItems)):
                test = lineItems[i]["name"] # e.g. "size", "font color"
                value = lineItems[i]["value"] # e.g. "large", "blue"
                productCustoms[productID][test] = value # adding customs to product

def printer():
    for i in range(0, len(prodIDs)):
        #print(i + 1)
        print("ID Number: ", IDNumbers[i])
        print("Order Number: ", orderNumbers[i])
        print("Product ID: ", int(IDproducts[i]), "\n", productCustoms[prodIDs[i]], "\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

orderSearch()
printer()

#print(productCustoms)
#print()
#print(len(productCustoms))
# print(len(IDNumbers))
# print(len(IDproducts))
# print(len(prodIDs))
