'''
Created on 24 oct 2024

@author: alber
'''

from _ast import Try

def P2(n: int, k: int, i: int = 1) -> int:
    assert n > 0, 'n debe ser un número positivo'
    assert k > 0, 'k debe ser un número positivo'
    assert i > 0, 'i debe ser un número positivo'
    assert i < k+1, 'i debe ser menor que k+1'
    assert n>= k, 'n debe ser mayor o igual que k'
    producto = 1
    for j in range(i, k - 1):
        producto *= (n - j + 1)
    
    return producto


print(P2(8,7))

from math import factorial

def C2(n,k):
    assert n>k, 'n debe ser mayor que k'
    assert n>0, 'n debe ser mayor que 0'
    assert k>0, 'k debe ser mayor que 0'
    
    return  factorial(n)// (factorial(k + 1)*factorial(n-k + 1))

print(C2(30,12))



def numero_combinatorio(n,k):
    if k > n:
        return 'k debe ser menor que n'
    else:
        return factorial(n)// (factorial(k)*factorial(n-k))

def S2(n,k):

    assert n>=k,'n debe ser mayor o gual que k'
    assert n>0, 'n debe ser mayor que 0'
    assert k>0, 'k deber ser mayor que 0'
    
    suma=0
    for i in range(k +1):
        numerador=((-1)**i)*numero_combinatorio(k,i)*((k-i)**(n+1))
        suma += numerador
    return (suma/(factorial(k+2)*n))
                
                
print(S2(5,3))


from typing import List, Tuple
from collections import Counter
import re

def palabras_mas_comunes(fichero,n: int=1) -> List[Tuple[str, int]]:  
    assert n>1, 'n debe ser mayor que 1'
    
    with open(fichero,'r', encoding='utf-8') as f:
        texto = f.read().lower()
        palabras = re.findall(r'\b\w+\b', texto)
        contador_palabras= Counter(palabras)
        mas_comunes= contador_palabras.most_common(n)
    return mas_comunes








def probar_P2():
    
    print('casos validos')
    
    try:
        assert P2(8,7) == 6720
        print('prueba 1 paso correcmtamente')
    except AssertionError:
        print('Error, prueba 1 fallo')
        
    
    try:
        assert P2(10, 7, 2) == 3024
        print('prueba 2 paso correctamente')
    except AssertionError:
        print('Error, prueba 2 fallo')
        
        
    print('casos no validos')
    
    try:
        P2(-1, 5)
    except AssertionError as e:
        print(f"Prueba 3: Fallo  AssertionError: {e}")
        


print(probar_P2())



def probar_C2():
    print('casos validos')
    
    try:
        assert C2(30,12) == 350175
        print('prueba 1 paso correcmtamente')
    except AssertionError:
        print('Error, prueba 1 fallo')
        
        
    print('casos no validos')
    
    try:
        C2(-1, 5)
    except AssertionError as e:
        print(f"Prueba 2: Fallo  AssertionError: {e}")
    
    
    
print(probar_C2())


def probar_S2():
    print('casos validos')
    
    try:
        assert S2(5,3) == 0.9
        print('prueba 1 paso correcmtamente')
    except AssertionError:
        print('Error, prueba 1 fallo')
        
        
    print('casos no validos')
    
    try:
        S2(-1, 5)
    except AssertionError as e:
        print(f"Prueba 3: Fallo  AssertionError: {e}")