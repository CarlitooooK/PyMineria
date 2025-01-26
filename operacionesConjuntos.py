import random

def eliminar_repetidos(lista):
    return list(set(lista))

def union(A, B):
    return list(set(A).union(B))

def interseccion(A, B):
    return list(set(A).intersection(B))

def diferencia(A, B):
    return list(set(A).difference(B))

def complemento(A, universo):
    return list(set(universo).difference(A))

E = [random.randint(1, 101) for _ in range(30)]
C = random.sample(E, 3)
D = random.sample(E, 9)
G = random.sample(E, 10)

E = eliminar_repetidos(E)
C = eliminar_repetidos(C)
D = eliminar_repetidos(D)
G = eliminar_repetidos(G)

print(f"CONJUNTO E: {E}")
print(f"CONJUNTO C: {C}")
print(f"CONJUNTO D: {D}")
print(f"CONJUNTO G: {G}\n")

resultado_union = union(E, C)
resultado_interseccion = interseccion(E, D)
resultado_diferencia = diferencia(E, G)

print(f"UNIÓN (E ∪ C): {resultado_union}")
print(f"INTERSECCIÓN (E ∩ D): {resultado_interseccion}")
print(f"DIFERENCIA (E - G): {resultado_diferencia}")