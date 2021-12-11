#mp.tf calculator program
from tkinter import *

#get properties
prop = [line.rstrip() for line in open('properties.txt', "r")]
propKey = float(prop[1])
propRef = float(prop[2])

itemKeyPrice = 0
itemRef = 0
SellPrice = 0

# function executed when 'go' is pressed
def go():
    #get forms
    itemKeyPrice = float(keys.get())
    itemRef = float(ref.get())
    SellPrice = float(dollar.get())
    mpKeyPrice = float(keyPrice.get())
    refValue = float(refPrice.get())
    a = itemRef / refValue; itemKeyPrice = itemKeyPrice + a; itemKeyPrice = round(itemKeyPrice, 2)

    #calc time
    #calculate price of key after discount
    if discountVar.get() == 1:
        a = mpKeyPrice * 10; mpKeyPriceDiscount = a / 11
        keyPriceStr = "Discounted "
    else:
        mpKeyPriceDiscount = mpKeyPrice
        keyPriceStr = ""
    #Cost of item bought, in dollars in relation to discounted mp.tf key prices)
    itemDollarPrice = itemKeyPrice * mpKeyPriceDiscount
    #money you'll get in return, after tax
    if SellPrice <= 0.05:
        b = 0
    else:
        b = SellPrice / 10
    sellReturn = SellPrice - b
    #calculate profit
    profit = sellReturn - itemDollarPrice
    
    #rounding
    mpKeyPriceDiscount = round(mpKeyPriceDiscount, 2)
    itemDollarPrice = round(itemDollarPrice, 2)
    sellReturn = round(sellReturn, 2)
    profit = round(profit, 2)

    #percentage profit
    c = profit / itemDollarPrice; percentProfit = c * 100
    #round rest
    percentProfit = round(percentProfit, 2)


    #result time
    #info collected
    text.configure(state='normal')
    text.delete(1.0, END)
    text.insert(END, "Current Key Price: {}\nPurchased item price, in keys: {} keys\nPrice to be sold as on mp.tf: {}\n\n{}Key Price: {}\nConverted Item Price: {}\nReturn After Tax: {}\nProfit: {}\n\nProfit Percentage: {}%".format(mpKeyPrice, itemKeyPrice, SellPrice, keyPriceStr, mpKeyPriceDiscount, itemDollarPrice, sellReturn, profit, percentProfit))
    text.configure(state='disabled')
    
# function executed when Clear is pressed
def clear():
    text.delete(1.0, END)
    keys.delete(0, END)
    ref.delete(0, END)
    dollar.delete(0, END)
    #reset properties file incase edited
    prop = [line.rstrip() for line in open('properties.txt', "r")]
    propKey = float(prop[1])
    propRef = float(prop[2])
    keyPrice.delete(0, END)
    refPrice.delete(0, END)
    keyPrice.insert(END, propKey)
    refPrice.insert(END, propRef)
    discountVar.set(1)
    

#create a fixed size window
root = Tk()
root.geometry("655x365")
root.title("Marketplace.tf Profit Calculator")
root.resizable(False,False)
root.configure(background="orange")
root.iconbitmap('favicon.ico')

#place a frame containing the input
frame_input = Frame(root)
frame_input.grid(row=0, column=0, columnspan=2, padx=15, pady=10)

#place the labels
Label(frame_input, text="Buy Price", width=22, anchor="w",font=('Impress BT',12)).grid(row=0, column=0, columnspan=3, padx=0, pady=0)
Label(frame_input, text="keys", width=9, anchor="w").grid(row=1, column=2, padx=5, pady=0)
Label(frame_input, text="ref", width=9, anchor="w").grid(row=2, column=2, padx=5, pady=0)
Label(frame_input, text="Sell Price", width=22, anchor="w",font=('Impress BT',12)).grid(row=3, column=0, columnspan=3, padx=5, pady=0)
Label(frame_input, text="dollars", width=9, anchor="w").grid(row=4, column=2, padx=5, pady=0)
Label(frame_input, text="Config", width=22, anchor="w",font=('Impress BT',12)).grid(row=5, column=0,columnspan=3, padx=5, pady=0)
Label(frame_input, text="Key price", width=9, anchor="w").grid(row=6, column=2, padx=5, pady=0)
Label(frame_input, text="Ref value", width=9, anchor="w").grid(row=7, column=2, padx=5, pady=0)

#checkbox for discount
discountVar = IntVar(value=1)
discount = Checkbutton(frame_input, text='Uncle Discount?', variable=discountVar, onvalue=1, offvalue=0).grid(row=8, columnspan=3, column=0, padx=5, pady=5)

#place the text entry fields
keys = Entry(frame_input, width=15, bg="white")
keys.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
ref = Entry(frame_input, width=15, bg="white")
ref.grid(row=2, column=0, padx=10, columnspan=2, pady=5)
dollar = Entry(frame_input, width=15, bg="white")
dollar.grid(row=4, column=0, padx=10, columnspan=2, pady=5)
keyPrice = Entry(frame_input, width=15, bg="white")
keyPrice.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
refPrice = Entry(frame_input, width=15, bg="white")
refPrice.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

#ref/key inserts
keyPrice.insert(END, propKey)
refPrice.insert(END, propRef)

#place a frame containing the go/clear buttons
frame_buttons = Frame(root)
frame_buttons.grid(row=1, column=0, columnspan=1, padx=2, pady=5)

#place the Go and Clear buttons
go_button = Button(frame_buttons, text="Go", width=7, command=go)
go_button.grid(row=0, column=0, padx=5, pady=5)
clear_button = Button(frame_buttons, text="Reset", width=7, command=clear)
clear_button.grid(row=1, column=0, padx=5, pady=5)

#option menu frame
frame_option = Frame(root)
frame_option.grid(row=1, column=1, columnspan=1, padx=0, pady=0)


#optionmenu
tkvar = StringVar(root)
choices = { 'Light blue','orange','purple','green','red'}
tkvar.set('orange')
popupMenu = OptionMenu(frame_option, tkvar, *choices)
Label(frame_option, text="Theme Selection").grid(row = 0, column = 0, padx=0, pady=5)
popupMenu.grid(row = 1, column =0, pady=5)

#what option menu does
# on change dropdown value
def change_dropdown(*args):
    root.configure(background=tkvar.get())
# link function to change dropdown
tkvar.trace('w', change_dropdown)

#heading?
frame_heading = Frame(root)
frame_heading.grid(row=1, column=2, columnspan=6, padx=0, pady=0)
Label(frame_heading,text="Bogg softawre :))",font=('Comic Sans MS',32)).grid(row=0,column=0,padx=0,pady=0)


#place the frame containing the output
frame_output = Frame(root)
frame_output.grid(row=0, column=2, columnspan=6, rowspan=1, padx=0, pady=5)

#place the output
text = Text(frame_output, state='disabled', height=15, width=50)
text.grid(row=0, column=0, padx=10, pady=5)

#run the whole program and draw window
root.mainloop()


