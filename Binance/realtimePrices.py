
from binance.client import Client
import json
import time
from Tkinter import *



WAIT_TIME = 3


client = Client(
"vMCHrzHzbwfQJRU9Lrgw7XrRTWUdWIwtFP2zFJbC2NfW7iJvFDxzp1fIKhgoQDo1",
"XfFBbOvSI55VH1jaq3Q9ADFfP2GqRrLdc6YE1z0QZToLRc1BgBbiQhLh5ZiBTDSG")


# get all symbol prices
tickers = client.get_all_tickers()
info = client.get_account()


tickersDic = {}
for i in tickers:
    tickersDic[i["symbol"]] = i["price"]


def tickerPrice(ticker):
    for t in tickers:
        if t["symbol"] == ticker:
            price = t["price"]
            #print "{} Price is {}".format(ticker,t["price"])
        else:
            print "price not found check ticker name"
            price = 0

    return price


def Price(ticker):
    try:
        return float(tickersDic[ticker])
    except:
        return 0


#MY ASSETS
def myAssets():
    lst = []
    for b in info["balances"]:
        if float(b["free"])  > 0.0002 :
            Ass = {b["asset"]:b["free"]}
            lst.append(Ass)
            #print b["asset"],b["free"]
    return lst

def Start ():
    while True:

        startTime = time.time()

        tickerPrice("BTCUSDT")
        myAssets()

        endTime = time.time()

        if endTime - startTime < WAIT_TIME:
            time.sleep(WAIT_TIME - (endTime - startTime))

########################################
root = Tk()
root.title("HODL")

top = Frame(root,width = 900,height = 50, relief = SUNKEN)
top.pack(side=TOP)

f1 = Frame(root,width = 300,height = 500, bg = "grey", relief = SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width = 300,height = 500, bg = "white", relief = SUNKEN)
f2.pack(side=LEFT)

f3 = Frame(root,width = 300,height = 500, bg = "grey", relief = SUNKEN)
f3.pack(side=LEFT)


def buttonMaker(lst):
    for i in lst:
        b = Button(toolbar, text=i, width=6, command = callback )
        b.pack(side=LEFT, padx=2, pady=2)

def labelMaker(dic,frame):
    for i,e in enumerate(dic):
        Label(frame, text=e.keys(), relief=RIDGE,width=15).grid(row=i,column=0)
        Label(frame, text=e.values(), relief=SUNKEN,width=10).grid(row=i,column=1)

def SinglelabelMaker(lst,c):
    for i,e in enumerate(lst):
        Label(text=e, relief=RIDGE,width=15).grid(row=i,column=c)

def top(list):
    for i,e in enumerate(list):
        Label(text=e, relief=SUNKEN,width=15).grid(row=0,column=i)

input_var = StringVar()
operator = ""

def callback(test):

    global operator
    operator = str(test)

    input_var.set(operator)

    if len(operator) > 2:

        for widget in f3.winfo_children():
            widget.destroy()

        key = operator + "BTC"
        frameTrades = client.get_my_trades(symbol=key)
        #print len(frameTrades)

        for i,j in enumerate(frameTrades):
            for k,l in enumerate(j):
                Label(f3,font=("Helvetica", 10), text=l, relief=SUNKEN,width=9).grid(row=0,column=k)
                Label(f3,font=("Helvetica", 10), text=j[l], relief=SUNKEN,width=9).grid(row=i+1,column=k)


        #print frameTrades

    #print operator
##########################################

def main():

    toolbar = Frame(root)
    myTickers = myAssets()
    #dollar = tickerPrice("BTCUSDT")
    buttons = {}
    for i,e in enumerate(myTickers):

        key = str(e.keys()[0])+"BTC"

        try:
            trades = client.get_my_trades(symbol=key)


            if trades[0]["isBuyer"]:

                trade = "BUYER"
                bought = trades[0]["price"]
                qty = trades[0]["qty"]

            else:
                trade = "SELLER"
                bought = "-"
                qty = "-"
        except:
            trades = "NA"
            bought = "-"
            qty = "-"

        btcprice = Price(key)

        tickerQt = float(e.values()[0])
        tickerQt = "{0:.8f}".format(tickerQt)
        btcValue = float(e.values()[0])*float(btcprice)
        btcValue = "{0:.8f}".format(btcValue)

        buttons["butt{}".format(i)] = Button(f1, text=e.keys()[0], width=8, command =lambda  x1 = str(e.keys()[0]) : callback(x1))
        buttons["butt{}".format(i)].grid(row=i,column=0)

        Label(f1, text=tickerQt, relief=SUNKEN,width=10).grid(row=i,column=1) #QUATITY
        Label(f1, text=btcValue, relief=SUNKEN,width=10).grid(row=i,column=2) #BTC VALUE


    Entry(f2, textvariable=input_var, relief=SUNKEN, width=10).grid(row=0,column=0)




    root.mainloop()



if __name__ == '__main__':
    main()
