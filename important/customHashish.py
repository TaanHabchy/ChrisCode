# make a hashmap of all the custom items, the key will be the productIDs and the data will be what to do when you find that
# specific item
colors = ["Black", "White", "Red", "Pink", "Maroon", "Royal Blue", "Navy", \
          "Carolina Blue", "Shark Teal", "Athletic Yellow", "Bright Yellow", \
            "Sport Orange", "Purple", "Kelly Green", "Forest Green", "HI-Vis Green", \
                "Vegas Gold", "Shiny Gold", "Gold", "Shiny Silver", "Grey", "Brown"]

listOfColorLists = {}

listOfColorLists["Black"] = []
listOfColorLists["White"] = []
listOfColorLists["Red"] = []
listOfColorLists["Pink"] = []
listOfColorLists["Maroon"] = []
listOfColorLists["Royal Blue"] = []
listOfColorLists["Navy"] = []
listOfColorLists["Carolina Blue"] = []
listOfColorLists["Shark Teal"] = []
listOfColorLists["Athletic Yellow"] = []
listOfColorLists["Bright Yellow"] = []
listOfColorLists["Sport Orange"] = []
listOfColorLists["Purple"] = []
listOfColorLists["Kelly Green"] = []
listOfColorLists["Forest Green"] = []
listOfColorLists["High-Vis Green"] = []
listOfColorLists["Vegas Gold"] = []
listOfColorLists["Shiny Gold"] = []
listOfColorLists["Gold"] = []
listOfColorLists["Shiny Silver"] = []
listOfColorLists["Grey"] = []
listOfColorLists["Brown"] = []


class textData:
    text = ""
    font = ""

    def print(self):
        print("Text: " + self.text)
        print("Font: " + self.font)

    def textData(self):
        self.text = ""
        self.font = ""

    def setText(self, data):
        self.text = str(data)

    def getText(self):
        return self.text 

    def setFont(self, data):
        self.font = data
    
    def getFont(self):
        return self.font
    
"""
PushDataToList
    - 
Parameter:
    - Input: 
"""
def pushDataToList(text, color, font):
    myTextData = textData()
    myTextData.textData()
    myTextData.setText(text)
    myTextData.setFont(font)

    if color in listOfColorLists:
        listOfColorLists[color].append(myTextData)
    else:
        print("color not found: ", color)
        print('Text is: ', text)

def getDataFromLineItem(productID, item):
    
    def customPick(x):
        if len(item["properties"]) > 0:
            return item["properties"][x]["value"]

    #Custom Number
    # print(productID)
    # print(type(productID))
    if(productID == 626889097271):
        number = customPick(0)
        font = customPick(1)
        textColor = customPick(2)
        # print("inside custom Number")
        pushDataToList(number, textColor, font)

    #Customized Arm Sleeve
    elif(productID == 10834995656):
        text = customPick(0)
        font = customPick(1)
        textColor = customPick(2)
        textLength = customPick(3)
        pushDataToList(text, textColor, font)

    #Custom Text Number
    elif(productID == 1421879279671):
        number = customPick(0)
        numberFont = customPick(1)
        numberColor = customPick(2)
        text = customPick(3)
        textFont = customPick(4)
        textColor = customPick(5)
        pushDataToList(text, textColor, textFont)
        pushDataToList(number, numberColor, numberFont)

    #Custom Headband
    elif(productID == 1376623132727):
        text = customPick(0)
        font = customPick(1)
        textColor = customPick(2)
        pushDataToList(text, textColor, font)

    # Number Football Towel
    elif(productID == 1688836046903):
        number = customPick(1)
        

    #Custom Leg Sleeve
    elif(productID == 673478279223):
        text = customPick(0)
        font = customPick(1)
        textColor = customPick(2)
        pushDataToList(text, textColor, font)
    
    # else:
    #     print("Not a Custom Item" + item["name"])