import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import customHash as hash
from tkinter import messagebox

pageWidth = 600

# registering fonts
#pdfmetrics.registerFont(TTFont('Rounded', "Dosis-regular11.ttf"))

try:
    pdfmetrics.registerFont(TTFont('Burny', 'Burny.ttf'))
    pdfmetrics.registerFont(TTFont('Marker', 'Bangers.ttf'))
    pdfmetrics.registerFont(TTFont('Tough', 'BlackOpsOne-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('College', 'College.ttf'))
    pdfmetrics.registerFont(TTFont('Iceberg', 'Iceberg.ttf'))
    pdfmetrics.registerFont(TTFont('Roboto', 'Roboto-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('Jersey', 'sportsjersey.ttf'))
    pdfmetrics.registerFont(TTFont('Asos', 'Full Pack 2025.ttf'))
    pdfmetrics.registerFont(TTFont('Adventure', 'SF Fedora.ttf'))
    pdfmetrics.registerFont(TTFont('Sporty', 'Calibri-bold.TTF'))
    pdfmetrics.registerFont(TTFont('Rounded', "Dosis-regular.ttf"))
except:
    messagebox.showerror("Error", "Error: Cannot open a specific font")

"""
Gives a relative size to each font
"""

avgSize = 100
fontSizeHash = {}
fontSizeHash["Marker"] = avgSize + 15
fontSizeHash["Tough"] = avgSize + 25
fontSizeHash["College"] = avgSize + 35
fontSizeHash["Iceberg"] = avgSize
fontSizeHash["Roboto"] = avgSize + 15
fontSizeHash["Jersey"] = avgSize + 35
fontSizeHash["Asos"] = avgSize - 10
fontSizeHash["Adventure"] = avgSize
fontSizeHash["Sporty"] = avgSize
fontSizeHash["Burny"] = avgSize
fontSizeHash["Rounded"] = avgSize

"""
Takes a font name and returns the size of that font
"""
def findSize(font):
    return fontSizeHash[font]


"""
Creates a basic pdf with simple string written on it
I use this to help with debugging to make sure I can reach the writing portion of the program
"""
def tester():
    c = canvas.Canvas(os.path.expanduser('~') + '/Desktop/test.pdf')
    c.setPageSize((864, 1224))
    # print(os.path.dirname(sys.executable))
    print(os.path.expanduser('~'))
    #c.drawString(20, 20, "helo")
    c.save()


"""
Input: color of text
"""


def makePDF(color):
    currentWidth = 15  # the width that we will be writing at
    drawHeight = 1300  # top of pdf where we will start writing

    if (len(hash.colorDataHash[color]) != 0):  # if there are orders with that specific color
        c = canvas.Canvas(os.path.expanduser('~') + '/Desktop/PDFS/' + color + ".pdf")  # creating a pdf instance
        c.setPageSize((590, 1404))

        for i in range(len(hash.colorDataHash[color])):
            customText = hash.colorDataHash[color][i] # for each iteration, customText is a different customized text
            for j in range(customText.quantity):
                fontSize = findSize(customText.font)
                c.setFont(customText.font, fontSize)
                stringWidth = pdfmetrics.stringWidth(customText.text, customText.font,
                                             fontSize)  # gives the overall text width

                print("String width: " + str(stringWidth) + "\nText: " + customText.text + "\nCurrentWidth: " + str(currentWidth) + '\n')

                if currentWidth + stringWidth > 575:  # if the string when fully written is wider than the page
                    currentWidth = 15  # go back to the left side
                    drawHeight -= 105  # new line

                    if drawHeight <= 0:  # if we have filled the page
                        c.showPage()  # create new page
                        drawHeight = 1300  # start back up at the top
                        c.setFont(customText.font, fontSize)  # need to reassign font, idk why but you do

                c.drawString(currentWidth, drawHeight, customText.text)  # draws the string

                currentWidth += stringWidth + 10  # adds space for next text input
        try:
            c.scale(.5, .5)
            c.save()
        except:
            messagebox.showerror("ERROR", "File could not save!")




def makeAllPDFs():
    for color in hash.colorDataHash:
        makePDF(color)
