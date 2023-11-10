from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import customHashish as hash
import tkinter as tk

pageWidth = 600

# registering fonts
pdfmetrics.registerFont(TTFont('Marker', 'Bangers.ttf'))
pdfmetrics.registerFont(TTFont('Tough', 'BlackOpsOne-Regular.ttf'))
pdfmetrics.registerFont(TTFont('College', 'colleges.ttf'))
pdfmetrics.registerFont(TTFont('Iceberg', 'Iceberg.ttf'))
pdfmetrics.registerFont(TTFont('Roboto', 'Roboto-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Jersey', 'sportsjersey.ttf'))
pdfmetrics.registerFont(TTFont('Asos', 'full_Pack_2025.ttf'))
pdfmetrics.registerFont(TTFont('Adventure', 'SF Fedora.ttf'))
pdfmetrics.registerFont(TTFont('Sporty', 'Calibri Bold.TTF'))
pdfmetrics.registerFont(TTFont('Burny', 'Burny.ttf'))
pdfmetrics.registerFont(TTFont('Rounded', "Dosis-Medium.ttf"))

"""
Gives a relative size to each font
"""
avgSize = 90
fontSizeHash = {}
fontSizeHash["Marker"] = avgSize
fontSizeHash["Tough"] = avgSize - 5
fontSizeHash["College"] = avgSize
fontSizeHash["Iceberg"] = avgSize
fontSizeHash["Roboto"] = avgSize
fontSizeHash["Jersey"] = avgSize
fontSizeHash["Asos"] = avgSize - 5
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
    c = canvas.Canvas('pdfs/' + color + ".pdf", pagesize=letter)
    c.drawString(20, 20, "helo")
    c.save()

"""
Input: color of text
"""
def makePDF(color):
    currentWidth = 15 # the width that we will be writing at
    drawHeight = 670 # top of pdf where we will start writing
    c = canvas.Canvas("pdfs/" + color + ".pdf", pagesize=letter) # creating a pdf instance
    
    if (len(hash.colorDataHash[color]) != 0): # if there are orders with that specific color
        """
        
        """
        for i in range(len(hash.colorDataHash[color])):
            customText = hash.colorDataHash[color][i] # for each iteration, customText is a different customized text
            c.setFont(customText.font, findSize(customText.font))
            stringWidth = pdfmetrics.stringWidth(customText.text, customText.font, findSize(customText.font)) # gives the overall text width

            if currentWidth + stringWidth > pageWidth: # if the string when fully written is wider than the page
                currentWidth = 15 # go back to the left side
                drawHeight -= 144 # new line

                if drawHeight <= 0: # if we have filled the page
                    c.showPage() # create new page
                    drawHeight = 670 # start back up at the top
                    c.setFont(customText.font, findSize(customText.font)) # need to reassign font, idk why but you do

            c.drawString(currentWidth, drawHeight, customText.text) # draws the string
            currentWidth += stringWidth + 30 # adds space for next text input
    c.save()

def makeAllPDFs():
    for color in hash.colorDataHash:
        makePDF(color)