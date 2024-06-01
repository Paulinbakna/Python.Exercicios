lista= [1,1,2,3,4,4,5,6,7,7,8,8,9,10,10]

for i in lista:
    contador= lista.count(i)
    if  contador >= 2 :
        lista.remove(i)

print(lista)
