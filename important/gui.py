import tkinter as tk
import pdfWriter as pw
# Creating a text field
def makePDF():
    user_input = entry.get()
    # result_label.config(text=f"You entered: {user_input}")
   
    pw.makePDF(user_input)
    
    
    # pw.tester(user_input)

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
 
button = tk.Button(root, text="Make PDF", command=makePDF)

button.pack()

done_button = tk.Button(root, text="Done", command=close_window)
done_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()

"""
Gui will have text input for one color
"""