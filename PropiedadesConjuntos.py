#import practica1
from operacionesConjuntos import union, interseccion, complemento

conjuntoA=[1,2,3,4,5]
conjuntoB=[3,4,5,6,7,8,9,10]
conjuntoC=[5,6,7]
universo=[1,2,3,4,5,6,7,8,9,10,11]


def asociatividad_union(A,B,C):

    union1 = []
    union1 = union(A, union(B,C))

    union2 = []
    union2 = union(union(A,B), C)
    print(union1)
    print(union2)
    if(union1 == union2):
        print("Son iguales")
    else:
        print("No son iguales")
    

def asociatividad_interseccion(A,B,C):
     
    interseccion1 = []
    interseccion1 = interseccion(A, interseccion(B,C))
    
    interseccion2 = []
    interseccion2 = interseccion(interseccion(A,B), C)
    print(interseccion1)
    print(interseccion2)
    if(interseccion1 == interseccion2):
        print("Son iguales")
    else:
        print("No son iguales")
    

def distribuidad_interseccion(A,B,C):
    
    op1 = []
    op1 = interseccion(A, union(B,C))
     
    op2 = []
    op2 = union(interseccion(A,B), interseccion(A,C))
    print(op1)
    print(op2)
    if(op1 == op2):
        print("Son iguales")
    else:
        print("No son iguales")
    

def distribuidad_union(A,B,C):
    
    op1 = []
    op1 = union(A, interseccion(B,C))
     
    op2 = []
    op2 = interseccion(union(A,B), union(A,C))
    print(op1,op2)
    if(op1 == op2):
        print("Son iguales")
    else:
        print("No son iguales")
    

def complemento_union(A,B, universo):
    op1 = []
    op1 = complemento(union(A,B), universo)

    op2 = []
    op2 = interseccion(complemento(A,universo), complemento(B, universo))
    print(op1,op2)
    if(op1 == op2):
        print("Son iguales")
    else:
        print("No son iguales")
    

def complemento_interseccion(A,B,universo):
    op1 = []
    op1 = complemento(interseccion(A,B), universo)
    op1.sort
    op2 = []
    op2 = union(complemento(A, universo), complemento(B,universo))
    op2.sort
    print(op1,op2)
    if(op1 == op2):
        print("Son iguales")
    else:
        print("No son iguales")
    


asociatividad_union(conjuntoA,conjuntoB,conjuntoC)
asociatividad_interseccion(conjuntoA,conjuntoB,conjuntoC)
distribuidad_interseccion(conjuntoA,conjuntoB,conjuntoC)
distribuidad_union(conjuntoA,conjuntoB,conjuntoC)
complemento_union(conjuntoA,conjuntoB,universo)
complemento_interseccion(conjuntoA,conjuntoB,universo)