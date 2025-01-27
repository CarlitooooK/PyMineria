import random


E = list(range(10))
C = random.sample(E,5)
D = random.sample(E,2)
G = random.sample(E,7)


def union(conjuntoA, conjuntoB):
    resultado = conjuntoA.copy()  
    for item in conjuntoB:
        if item not in resultado:
            resultado.append(item)
    return resultado

def interseccion(conjuntoA, conjuntoB):
    resultado = []
    for item in conjuntoA:
        if item in conjuntoB and item not in resultado:
            resultado.append(item)
    return resultado

def diferencia(conjuntoA, conjuntoB):
    resultado = []
    for item in conjuntoA:
        if item not in conjuntoB:
            resultado.append(item)
    
    return resultado

a=[1,2,3]
b=[3,4,5,6]

union = union(a, b)
print(union)
interseccion = interseccion(a, b)
print(interseccion)
diferencia = diferencia(a, b)
print(diferencia)