lista = [0,1,1,2,0,0,0,1,2,0]

def combinator(lista,a,b):
    newlist = []
    for i in lista:

        if i == 0:
            newlist.append(a)
        else:
            newlist.append(b)

    return newlist


print combinator(lista,'patate','tomate')
print combinator(lista,'fragole','banane')
