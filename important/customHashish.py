# make a hashmap of all the custom items, the key will be the productIDs and the data will be what to do when you find that
# specific item
colors = ["Black", "White", "Red", "Pink", "Maroon", "Royal Blue", "Navy",
          "Carolina Blue", "Shark Teal", "Athletic Yellow", "Bright Yellow",
          "Sport Orange", "Purple", "Kelly Green", "Forest Green", "HI-Vis Green",
          "Vegas Gold", "Shiny Gold", "Gold", "Shiny Silver", "Grey", "Brown"]

colorDataHash = {}

colorDataHash["Black"] = []
colorDataHash["White"] = []
colorDataHash["Red"] = []
colorDataHash["Pink"] = []
colorDataHash["Maroon"] = []
colorDataHash["Royal Blue"] = []
colorDataHash["Navy"] = []
colorDataHash["Carolina Blue"] = []
colorDataHash["Shark Teal"] = []
colorDataHash["Athletic Yellow"] = []
colorDataHash["Bright Yellow"] = []
colorDataHash["Sport Orange"] = []
colorDataHash["Purple"] = []
colorDataHash["Kelly Green"] = []
colorDataHash["Forest Green"] = []
colorDataHash["High-Vis Green"] = []
colorDataHash["Vegas Gold"] = []
colorDataHash["Shiny Gold"] = []
colorDataHash["Gold"] = []
colorDataHash["Shiny Silver"] = []
colorDataHash["Grey"] = []
colorDataHash["Brown"] = []


class textData:
    text = ""
    font = ""

    def print(self):
        print("Text: " + self.text)
        print("Font: " + self.font)

    """
    
    Initiates instances of a text and font
    """

    def textData(self):
        self.text = ""
        self.font = ""

    """
    takes the data of the text and converts it into a string
    input: data
    output: String
    """

    def setText(self, data):
        self.text = str(data)

    def getText(self):
        return self.text

    """
    setText but for Font
    """

    def setFont(self, data):
        self.font = data

    def getFont(self):
        return self.font


"""
Parameters:
    - Input: text, color and font
    - Output: adds the customizable data to that text's respective color list
"""


def pushDataToList(text, color, font):
    myTextData = textData()
    myTextData.textData()
    myTextData.setText(text)
    myTextData.setFont(font)

    try:
        colorDataHash[color].append(myTextData)
    except ModuleNotFoundError:
        print(color + " is not in the list of colors")

    # if color in listOfColorLists: # if the color is in our list of colors
    #     listOfColorLists[color].append(myTextData)
    # else:
    #     print("color not found: ", color)
    #     print('Text is: ', text)


"""
Input: ProductID, item
"""


def getDataFromLineItem(productID, item):
    """
    If there are customizable properties return the customized
    """
    def customPick(x):
        if len(item["properties"]) > 0:
            return item["properties"][x]["value"]

    # Customizable Number
    if (productID == 626889097271):
        number = customPick(0)
        font = customPick(1)
        textColor = customPick(2)
        pushDataToList(number, textColor, font)

    # Customized Arm Sleeve
    elif (productID == 10834995656):
        text = customPick(0)
        font = customPick(1)
        textColor = customPick(2)
        textLength = customPick(3)
        pushDataToList(text, textColor, font)

    # Custom Text Number
    elif (productID == 1421879279671):
        number = customPick(0)
        numberFont = customPick(1)
        numberColor = customPick(2)
        text = customPick(3)
        textFont = customPick(4)
        textColor = customPick(5)
        pushDataToList(text, textColor, textFont)
        pushDataToList(number, numberColor, numberFont)

    # Custom Headband
    elif (productID == 1376623132727):
        text = customPick(0)
        font = customPick(1)
        textColor = customPick(2)
        pushDataToList(text, textColor, font)

    # Number Football Towel
    elif (productID == 1688836046903):
        number = customPick(1)

    # Custom Leg Sleeve
    elif (productID == 673478279223):
        text = customPick(0)
        font = customPick(1)
        textColor = customPick(2)
        pushDataToList(text, textColor, font)
