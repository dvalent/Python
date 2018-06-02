import Tkinter
import tkFont
import ttk

from binance.client import Client
import json
import time

tick_columns = ("country", "capital", "currency")
tree_data = [
    ("Argentina",      "Buenos Aires",     "ARS"),
    ("Australia",      "Canberra",         "AUD"),
    ("Brazil",         "Brazilia",         "BRL"),
    ("Canada",         "Ottawa",           "CAD"),
    ("China",          "Beijing",          "CNY"),
    ("France",         "Paris",            "EUR"),
    ("Germany",        "Berlin",           "EUR"),
    ("India",          "New Delhi",        "INR"),
    ("Italy",          "Rome",             "EUR"),
    ("Japan",          "Tokyo",            "JPY"),
    ("Mexico",         "Mexico City",      "MXN"),
    ("Russia",         "Moscow",           "RUB"),
    ("South Africa",   "Pretoria",         "ZAR"),
    ("United Kingdom", "London",           "GBP"),
    ("United States",  "Washington, D.C.", "USD")
    ]

client = Client(
"vMCHrzHzbwfQJRU9Lrgw7XrRTWUdWIwtFP2zFJbC2NfW7iJvFDxzp1fIKhgoQDo1",
"XfFBbOvSI55VH1jaq3Q9ADFfP2GqRrLdc6YE1z0QZToLRc1BgBbiQhLh5ZiBTDSG")


# get all symbol prices
tickers = client.get_all_tickers()
info = client.get_account()

tick_columns = ("SHITCOIN","BALANCE")

#MY ASSETS
def myAssets():
    lst = []
    for b in info["balances"]:
        btcValue = "{0:.8f}".format(float(b["free"]))
        name = str(b["asset"])
        
        if float(b["free"])  > 0.0002 :

            Ass = (name,btcValue)
            lst.append(Ass)
            #print b["asset"],b["free"]
    return lst


tick_columns = ("SHITCOIN","BALANCE")
tick_data = myAssets()



def sortby(tree, col, descending):
    """Sort tree contents when a column is clicked on."""
    # grab values to sort
    data = [(tree.set(child, col), child) for child in tree.get_children('')]

    # reorder data
    data.sort(reverse=descending)
    for indx, item in enumerate(data):
        tree.move(item[1], '', indx)

    # switch the heading so that it will sort in the opposite direction
    tree.heading(col,
        command=lambda col=col: sortby(tree, col, int(not descending)))

class App(object):
    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        msg = ttk.Label(wraplength="4i", justify="left", anchor="n",
            padding=(10, 2, 10, 6),
            text=("Welcomez to h0dl for Binancez TM"))
        msg.pack(fill='x')

        container = ttk.Frame()
        container.pack(fill='both', expand=True)

        # XXX Sounds like a good support class would be one for constructing
        #     a treeview with scrollbars.
        self.tree = ttk.Treeview(columns=tick_columns, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in tick_columns:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            # XXX tkFont.Font().measure expected args are incorrect according
            #     to the Tk docs
            self.tree.column(col, width=tkFont.Font().measure(col.title()))

        for item in tick_data:
            self.tree.insert('', 'end', values=item)

            # adjust columns lenghts if necessary
            for indx, val in enumerate(item):
                ilen = tkFont.Font().measure(val)
                if self.tree.column(tick_columns[indx], width=None) < ilen:
                    self.tree.column(tick_columns[indx], width=ilen)

def main():
    root = Tkinter.Tk()
    root.wm_title("Multi-Column List")
    root.wm_iconname("mclist")


    app = App()
    root.mainloop()

if __name__ == "__main__":
    main()
