import tkinter as tk

custDate = None

myDate = None

def close_window():
    root.destroy()


# Create a main window
root = tk.Tk()
root.title("Make PDFs")

# Create a label widget
label = tk.Label(root, text="Choose a date")
label.pack()

# entry for the date to be inputed, gets last 250 orders up to that date

date = tk.Entry(root)
custDate = date.get()
date.pack() 


def getDates():
    global custDate 
    custDate = date.get()
    print("In get date: ",custDate)
    return custDate

dateButton = tk.Button(root, text=("Submit Date"), command = lambda: getDates())
dateButton.pack()

# allButton = tk.Button(root, text="Make all PDFs", command = lambda: pw.makePDFs)
# allButton.pack()

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