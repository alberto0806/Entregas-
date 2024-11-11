'''
Created on 2 nov 2024

@author: alber
'''
from tipos.cola import Cola
def test_cola():
    print('TEST DE COLA:')
    print('\n##################')
    print('Creación de una cola vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5')
    
    colaa = Cola.of()
    elementos_añadir = [23,47,1,2,-3,4,5] 
    for e in elementos_añadir:
        colaa.add(e)
    
    print(f'Resultado de la cola: {colaa}')
    
    print('\n##################')
    elementos_eliminados = colaa.remove_all()
    print(f'Elementos eliminados utilizando remove_all:{elementos_eliminados}')
    
if __name__ == '__main__':
    test_cola()