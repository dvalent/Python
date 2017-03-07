myList = [0,50,100,205,206,209,210,211,215]


available = []
m = max(myList)

for i in range(0, max(myList)+1):
    if i in myList:
        pass
    else:
        available.append(i)

print available
