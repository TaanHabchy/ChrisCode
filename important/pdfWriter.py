from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import customHashish as hash

pageWidth = 600

# registering fonts
pdfmetrics.registerFont(TTFont('Marker', 'fonts/Bangers.ttf'))
pdfmetrics.registerFont(TTFont('Tough', 'fonts/BlackOpsOne-Regular.ttf'))
pdfmetrics.registerFont(TTFont('College', 'fonts/colleges.ttf'))
pdfmetrics.registerFont(TTFont('Iceberg', 'fonts/Iceberg.ttf'))
pdfmetrics.registerFont(TTFont('Roboto', 'fonts/Roboto-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Jersey', 'fonts/sportsjersey.ttf'))
pdfmetrics.registerFont(TTFont('Asos', 'fonts/full_Pack_2025.ttf'))
pdfmetrics.registerFont(TTFont('Adventure', 'fonts/SF Fedora.ttf'))
pdfmetrics.registerFont(TTFont('Sporty', 'fonts/Calibri Bold.TTF'))
pdfmetrics.registerFont(TTFont('Burny', 'fonts/Burny.ttf'))
pdfmetrics.registerFont(TTFont('Rounded', "fonts/Dosis-Medium.ttf"))

"""
Gives a relative size to each font
"""
avgSize = 100
fontSizeHash = {}
fontSizeHash["Marker"] = avgSize
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
def tester(color):
    c = canvas.Canvas(color + ".pdf", pagesize=letter)
    c.drawString(20, 20, "helo")
    c.save()


"""
Input: color of text
"""


def makePDF(color):
    currentWidth = 15  # the width that we will be writing at
    drawHeight = 670  # top of pdf where we will start writing

    if (len(hash.colorDataHash[color]) != 0):  # if there are orders with that specific color
        c = canvas.Canvas(color + ".pdf", pagesize=letter)  # creating a pdf instance

        for i in range(len(hash.colorDataHash[color])):
            customText = hash.colorDataHash[color][i] # for each iteration, customText is a different customized text
            for j in range(customText.quantity):
                c.setFont(customText.font, findSize(customText.font))
                stringWidth = pdfmetrics.stringWidth(customText.text, customText.font,
                                             findSize(customText.font))  # gives the overall text width

                if currentWidth + stringWidth > pageWidth:  # if the string when fully written is wider than the page
                    currentWidth = 15  # go back to the left side
                    drawHeight -= 105  # new line

                    if drawHeight <= 0:  # if we have filled the page
                        c.showPage()  # create new page
                        drawHeight = 670  # start back up at the top
                        c.setFont(customText.font, findSize(customText.font))  # need to reassign font, idk why but you do

                c.drawString(currentWidth, drawHeight, customText.text)  # draws the string
                currentWidth += stringWidth + 30  # adds space for next text input
        c.save()


def makeAllPDFs():
    for color in hash.colorDataHash:
        makePDF(color)
