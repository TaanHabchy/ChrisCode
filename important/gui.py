import tkinter as tk
import pdfWriter as pw


def close_window():
    root.destroy()

# Create a main window
root = tk.Tk()
root.title("Make one pdf")

# Create a label widget
label = tk.Label(root, text="Choose a Color")
label.pack()

entry = tk.Entry(root)
entry.pack()    
 
button = tk.Button(root, text="Make PDF", command=lambda: makePDF(entry.get()))

button.pack()

done_button = tk.Button(root, text="Done", command=lambda: close_window())
done_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()

"""
Gui will have text input for one color
"""
