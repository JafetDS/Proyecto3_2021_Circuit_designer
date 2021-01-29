
# Retorna la Lista Invertida
def insertsort(lista):
    for i in range(1,len(lista)):
        pos = i
        while pos > 0 and lista[pos-1] > lista[i]:
            pos -= 1
        lista = lista[:pos] + [lista[i]] + lista[pos:i] + lista[i+1:]
    return lista.reverse()


#Retorna La lista Normal
def qsaux(lista):
    if len(lista)==1 or len(lista)==0:
        return lista
    else:
        pivote = lista[-1]
        menores = [x for x in lista[:-1] if x < pivote]
        mayores = [x for x in lista[:-1] if x >= pivote]
        return qsaux(menores) + [pivote] + qsaux(mayores)

