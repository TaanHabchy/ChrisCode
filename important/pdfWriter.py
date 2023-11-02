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

avgFont = 90
fonts = {}
fonts["Marker"] = avgFont
fonts["Tough"] = avgFont - 5
fonts["College"] = avgFont
fonts["Iceberg"] = avgFont
fonts["Roboto"] = avgFont
fonts["Jersey"] = avgFont
fonts["Asos"] = avgFont - 5
fonts["Adventure"] = avgFont
fonts["Sporty"] = avgFont
fonts["Burny"] = avgFont
fonts["Rounded"] = avgFont


def fontSize(font):
    return fonts[font]


def tester(color):
    c = canvas.Canvas('pdfs/' + color + ".pdf", pagesize=letter)
    c.drawString(20, 20, "helo")
    c.save()


def makePDF(color):
    print("color is", color)
    currentWidth = 15
    drawHeight = 680
    c = canvas.Canvas("pdfs/" + color + ".pdf", pagesize=letter)

    
    print("Length: ", len(hash.listOfColorLists[color]))
    if (len(hash.listOfColorLists[color]) != 0):
        
        for i in range(len(hash.listOfColorLists[color])):
            custom = hash.listOfColorLists[color][i]
            c.setFont(custom.font, fontSize(custom.font))
            stringWidth = pdfmetrics.stringWidth(
                custom.text, custom.font, fontSize(custom.font))

            if currentWidth + stringWidth > pageWidth:
                currentWidth = 15
                drawHeight -= 144

                if drawHeight <= 0:
                    c.showPage()
                    drawHeight = 710
                    c.setFont(custom.font, fontSize(custom.font))

            c.drawString(currentWidth, drawHeight, custom.text)
            currentWidth += stringWidth + 30
    c.save()


def makePDFs():

    for color in hash.listOfColorLists:
        drawHeight = 690
        currentWidth = 15
        # print("The currentHeight is: ", drawHeight, " for color: ", color)
        drawHeight = 720
        c = canvas.Canvas("pdfs/" + color + ".pdf", pagesize=letter)

        if (len(hash.listOfColorLists[color]) != 0):
            for i in range(len(hash.listOfColorLists[color])):
                custom = hash.listOfColorLists[color][i]
                c.setFont(custom.font, fontSize(custom.font))
                stringWidth = pdfmetrics.stringWidth(
                    custom.text, custom.font, fontSize(custom.font))

                if currentWidth + stringWidth > pageWidth:
                    currentWidth = 15
                    drawHeight -= 144

                    if drawHeight <= 0:
                        c.showPage()
                        drawHeight = 710
                        c.setFont(custom.font, fontSize(custom.font))

                c.drawString(currentWidth, drawHeight, custom.text)
                currentWidth += stringWidth + 30
        c.save()