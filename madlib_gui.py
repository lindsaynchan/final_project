import madlib

from Tkinter import *

root_widget = Tk()                          # creates a widget window which will hold all other widgets.
root_widget.geometry("700x700")             # sets the size of the window
root_widget.title("Madlibs")        # set the title of the window

var_label_text = StringVar()                # Special Tkinter Variable for label text
var_label_text.set("Welcome to Madlibs!\n\nPlease select an option.")
lbl_menu = Label(root_widget, textvariable=var_label_text)
lbl_menu.grid(row=1,column=1)                            # show the label

var_label_text1 = StringVar()
var_label_text1.set("0 - Main Menu")
lbl_main = Label(root_widget, textvariable=var_label_text1)
lbl_main.grid(row=2,column=1)

var_label_text2 = StringVar()
var_label_text2.set("1 - Pick a Madlib")
lbl_pick = Label(root_widget, textvariable=var_label_text2)
lbl_pick.grid(row=3,column=1)


entry_text = Entry()                        # creates a text entry box
entry_text.insert(0, "")   # text to display on start up
entry_text.pack()

# create a button
# command sets a function to run when the button is clicked. AKA as an event and callback
btn_ok = Button(text='Ok', command=lambda: madlib.main(entry_text))
btn_ok.pack()

# runs the window in a loop so it continuously detects the button click event
root_widget.mainloop()

