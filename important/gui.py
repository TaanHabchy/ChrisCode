import tkinter as tk
import main as m
import pdfWriter as pw

custDate = None
custLimit = None
custID = None

def close_window():
    root.destroy()

def getDates():
    global custDate 
    custLimit = limitEntry.get()
    return custDate


# Create a main window
root = tk.Tk()
root.title("Make PDFs")
root.geometry("300x300")

limitLabel = tk.Label(root, text="How many orders do you want?")
limitLabel.pack()

limitEntry = tk.Entry(root)
# custDate = date.get()
limitEntry.pack()

lastOrderID = tk.Label(root, text="Input the last ID")
lastOrderID.pack()

lastOrderIDEntry = tk.Entry(root)
lastOrderIDEntry.pack()

searchButton = tk.Button(root, text="Search Data", command=lambda: m.completeSearch)
searchButton.pack()


PDFButton = tk.Button(root, text="Make all PDFs", command = lambda: pw.makePDFs)
PDFButton.pack()

done_button = tk.Button(root, text="Done", command=lambda: close_window())
done_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()

"""
import tkinter as tk

custDate = None

def close_window():
    root.destroy()

def getDates():
    global custDate 
    custDate = date.get()
    print("In get date:", custDate)
    return custDate

def mainGui():
    global root, date

    root = tk.Tk()
    root.title("Make PDFs")

    label = tk.Label(root, text="Choose a date")
    label.pack()

    date = tk.Entry(root)
    date.pack()

    dateButton = tk.Button(root, text=("Submit Date"), command=lambda: getDates())
    dateButton.pack()

    done_button = tk.Button(root, text="Done", command=close_window)
    done_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    mainGui()

"""