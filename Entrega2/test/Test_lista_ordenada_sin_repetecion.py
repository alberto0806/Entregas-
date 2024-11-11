'''
Created on 2 nov 2024

@author: alber
'''
from tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticion
def test_lista_ordenada_sin_repeticion():
    print("TEST DE LISTA ORDENADA SIN REPETICIÓN:")
    print("################################################")
    print("Creación de una lista con criterio de orden lambda x: -x")
    lista = Lista_ordenada_sin_repeticion.of(lambda x: -x)
    
    print("Se añade en este orden: 23, 47, 47, 1, 2, -3, 4, 5")
    lista.add(23)
    lista.add(47)
    lista.add(47)
    lista.add(1)
    lista.add(2)
    lista.add(-3)
    lista.add(4)
    lista.add(5)
    
    print(f"Resultado de la lista ordenada sin repetición: {lista}")
    
    print("################################################")
    print(f"El elemento eliminado al utilizar remove(): {lista.remove()}")
    
    print("################################################")
    print(f"Elementos eliminados utilizando remove_all: {lista.remove_all()}")
    
    print("################################################")
    print("Comprobando si se añaden los números en la posición correcta...")
    lista.add(47)
    lista.add(23)
    lista.add(5)
    lista.add(4)
    lista.add(2)
    lista.add(1)
    lista.add(0)
    lista.add(-3)
    print(f"Lista después de añadirle el 0: {lista}")
    
    lista.add(0)
    print(f"Lista después de añadirle el 0: {lista}")
    
    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}")

if __name__ == "__main__":
    test_lista_ordenada_sin_repeticion()
    
    
    
    
    
    
