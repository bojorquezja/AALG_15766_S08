def sumRes(lista):
    if len(lista) == 0:
        return 0
    else:
        return sumaresta(lista, len(lista) - 1)

def sumaresta(lista, x) -> int:
    if x == 0:
        #print(f"{x}")
        z = lista[x] if lista[x] % 2 == 0 else - lista[x]
        #print(f"{z} {x}")
        return z
    else:
        #print(f"{x}")
        z = sumaresta(lista, x - 1) + (lista[x] if lista[x] % 2 == 0 else - lista[x])
        #print(f"{z} {x}")
        return z

       

lista = [2,3,8,1]
resultado = sumRes(lista) #10-4=6
print(resultado)
