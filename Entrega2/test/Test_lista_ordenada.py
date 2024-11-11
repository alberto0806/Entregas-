'''
Created on 2 nov 2024

@author: alber
'''
from tipos.Lista_ordenada import Lista_ordenada

def test_lista_ordenada():
    print("TEST DE LISTA ORDENADA:")
    print("################################################")
    print("Creación de una lista con criterio de orden lambda x: x")
    lista = Lista_ordenada.of(lambda x: x)
    
    print("Se añade en este orden: 3, 1, 2")
    lista.add(3)
    lista.add(1)
    lista.add(2)
    
    print(f"Resultado de la lista: {lista}")
    
    print("\n################################################")
    print(f"El elemento eliminado al utilizar remove(): {lista.remove()}")
    
    print("\n################################################")
    print(f"Elementos eliminados utilizando remove_all: {lista.remove_all()}")
    
    print("\n################################################")
    print("Comprobando si se añaden los números en la posición correcta...")
    lista.add(1)
    lista.add(3)
    lista.add(2)
    lista.add(0)
    print(f"Lista después de añadirle el 0: {lista}")
    
    lista.add(10)
    print(f"Lista después de añadirle el 10: {lista}")
    
    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}")

if __name__ == "__main__":
    test_lista_ordenada()
    


