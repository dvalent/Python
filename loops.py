listanumeri = [0,1,2,3,4,5.643,345,234,1,14,5345]

famiglie = [["gianni",'olga','david','sara'],["omi","andrea"],["cristina","alessandro","vanessa"]]


numeroimportante = listanumeri[6]


#print numeroimportante

nuovalista = []

for item in listanumeri:
    #do something
    x = item * 2
    nuovalista.append(x)


#print nuovalista[6]

newfamily = [(f.append('valentina')) for f in famiglie]
