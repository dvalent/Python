from Tkinter import *

root = Tk()
root.title("HODL")

pressed = ""

tickers = ["AA","BB","CC","DD","EE","FF"]

def buttonMaker(lst):
    for i in lst:
        b = Button(toolbar, text=i, width=6, command = callback )
        b.pack(side=LEFT, padx=2, pady=2)

def labelMaker(dic):
    for i,e in enumerate(dic):
        Label(text=e, relief=RIDGE,width=15).grid(row=i,column=0)
        Label(text=e, relief=SUNKEN,width=10).grid(row=i,column=1)

def callback():
    global pressed
    print "callback!!!"


# create a toolbar
toolbar = Frame(root)

labelMaker(tickers)


mainloop()
