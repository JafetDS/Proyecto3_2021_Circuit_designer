class Ordenamiento():
    def __init__(self):
        pass
    # Retorna la Lista Invertida
    @staticmethod
    def insertsort(lista):
        for i in range(1,len(lista)):
            pos = i
            while pos > 0 and lista[pos-1] > lista[i]:
                pos -= 1
            lista = lista[:pos] + [lista[i]] + lista[pos:i] + lista[i+1:]
        return lista[::-1]


    #Retorna La lista Normal
    @staticmethod
    def qsaux(lista):
        if len(lista) == 1 or len(lista)==0:
            return lista
        else:
            pivote = lista[-1]
            menores = [x for x in lista[:-1] if x < pivote]
            mayores = [x for x in lista[:-1] if x >= pivote]
            return Ordenamiento.qsaux (menores) + [pivote] + Ordenamiento.qsaux (mayores)

