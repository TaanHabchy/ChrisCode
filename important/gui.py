import tkinter as tk
import datasearch as ds
import pdfWriter as pw

idLen = 14

def on_validate(new_value):
    return len(new_value) == 14  # Limit the input to 10 characters


def close_window():
    root.destroy()

def getDates():
    global custDate 
    custLimit = limitEntry.get()
    return custDate

def search_action():
    id_value = lastOrderIDEntry.get()
    if len(id_value) == idLen:
        # Perform the search or any action here
        ds.completeSearch(limitEntry.get(), id_value)
    else:
        print("ID should be exactly 14 digits.")

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

validCommand = root.register(on_validate)

lastOrderIDEntry = tk.Entry(root, validate="key", validatecommand=validCommand)
lastOrderIDEntry.pack()

searchButton = tk.Button(root, text="Search Data", command=lambda: ds.completeSearch(limitEntry.get(), lastOrderIDEntry.get()))
searchButton.pack()

PDFButton = tk.Button(root, text="Make all PDFs", command = lambda: pw.makeAllPDFs())
PDFButton.pack()

done_button = tk.Button(root, text="Done", command=lambda: close_window())
done_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()