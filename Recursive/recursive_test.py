myList = [0,50,100,205,206,209,210,211,215]


available = []



def check(list,index,counter = 1):
    current = list[index]
    previous = list[index-1]

    if current != previous+counter:
        available.append(previous+counter)
        counter += 1
        check(list,index,counter)









for i,n in enumerate(myList):
    if i >= 1:
        check(myList,i)


print available
