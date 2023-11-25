import tkinter as tk
from tkinter import messagebox
import dataSearch as ds
import pdfWriter as pw


def close_window():
    root.destroy()

def getDates():
    global custDate
    custLimit = limitEntry.get()
    return custDate

def search_action(limit, id):
    if(len(id) != 13):
        IDerror()

    if(len(limit) == 0):
        limitError()

    ds.completeSearch(limit, id)

def IDerror():
    messagebox.showerror("Error with ID number", "Error: the ID is invalid")

def limitError():
    messagebox.showerror("Error with limit", "Error: number of orders is invalid")

# Create a main window
root = tk.Tk()
root.title("Custom Sports Sleeves")
root.geometry("300x300")

limitLabel = tk.Label(root, text="How many orders do you want?")

limitLabel.pack()

limitEntry = tk.Entry(root)
limitEntry.pack()

lastOrderID = tk.Label(root, text="Since Order ID *GET FROM SHOPIFY*")
lastOrderID.pack()

lastOrderIDEntry = tk.Entry(root)
lastOrderIDEntry.pack()

searchButton = tk.Button(root, text="Search Data", command=lambda: search_action(limitEntry.get(), lastOrderIDEntry.get()))
searchButton.pack()

PDFButton = tk.Button(root, text="Make all PDFs", command=lambda: pw.makeAllPDFs())
PDFButton.pack()

done_button = tk.Button(root, text="Done", command=lambda: close_window())
done_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()
