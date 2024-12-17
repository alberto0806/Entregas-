'''
Created on 16 dic 2024

@author: alber
'''

from grafo.grafo1 import Grafo
from grafo.red_social import *
def test_grafo():
    raiz = '../../' # Cambia esta variable si ejecutas este script desde otro directorio
    rrss = Red_social.parse(raiz+'resources/usuarios.txt', raiz+'resources/relaciones.txt', es_dirigido=False)

    print("************** Nº Predecesores de cada vértice")
    for usuario in rrss.vertices():
        print(f"{usuario} -- {len(rrss.predecessors(usuario))}")

    print("\n************** Nº Vecinos de cada vértice")
    for usuario in rrss.vertices():
        print(f"{usuario} -- {len(rrss.successors(usuario))}")

def test_recorrido_en_anchura():
    raiz = '../../' # Cambia esta variable si ejecutas este script desde otro directorio
    rrss = Red_social.parse(raiz+'resources/usuarios.txt', raiz+'resources/relaciones.txt', es_dirigido=False)

    inicio = rrss.usuarios_dni['25143909I']
    fin = rrss.usuarios_dni['87345530M']

    print("El camino más corto desde 25143909I hasta 87345530M es:")
    camino = bfs(rrss, inicio, fin)
    if camino:
        print([str(usuario) for usuario in camino])
        print(f"La distancia mínima es: {len(camino) - 1} pasos.")
    else:
        print("No se encontró un camino entre los usuarios especificados.")

def test_recorrido_en_profundidad():
    raiz = '../../' # Cambia esta variable si ejecutas este script desde otro directorio
    rrss = Red_social.parse(raiz+'resources/usuarios.txt', raiz+'resources/relaciones.txt', es_dirigido=False)
    
    inicio = rrss.usuarios_dni['25143909I']
    fin = rrss.usuarios_dni['76929765H']

    camino = dfs(rrss, inicio, fin)
    if camino:
        print(f"Hay un camino entre 25143909I y 76929765H:")
        print([str(usuario) for usuario in camino])
    else:
        print("No hay conexión directa entre 25143909I y 76929765H.")

if __name__ == "__main__":
    print("Test del grafo:")
    test_grafo()
    print("\nTest de recorrido en anchura:")
    test_recorrido_en_anchura()
    print("\nTest de recorrido en profundidad:")
    test_recorrido_en_profundidad()






