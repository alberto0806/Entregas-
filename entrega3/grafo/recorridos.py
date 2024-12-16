'''
Created on 21 nov 2024

@author: damat

-------------
Pseudocódigo:
-------------

función bfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una cola vacía
    agregar inicio a la cola
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la cola no esté vacía:
        tomar el elemento que está al frente de la cola y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo:
                si vecino no está en visitados:
                    agregar vecino a la cola
                    registrar a vértice como predecesor de vecino en predecesores

    devolver reconstruir_camino(predecesores, destino)

-------------------------------------------------------------
función dfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una pila vacía
    agregar inicio a la pila
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la pila no esté vacía:
        tomar el elemento más reciente agregado a la pila y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo, en orden inverso:
                si vecino no está en visitados:
                    agregar vecino a la pila
                    registrar a vértice como predecesor de vecino en predecesores

    devolver reconstruir_camino(predecesores, destino)
-------------------------------------------------------------------------

función reconstruir_camino(predecesores, destino):
    crear una lista vacía llamada camino
    establecer vértice_actual como destino

    mientras vértice_actual no sea nulo:
        agregar vértice_actual al inicio de la lista camino
        cambiar vértice_actual al predecesor de dicho vértice_actual usando el diccionario predecesores

    devolver camino

'''
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Set, Dict, Optional
from grafo.grafo1 import Grafo
from grafo.estructuras import Cola
from grafo.estructuras import Pila

# Importa la clase Grafo desde su módulo

V = TypeVar('V')  # Tipo de los vértices
E = TypeVar('E')  # Tipo de las aristas

class Recorrido(ABC, Generic[V, E]):
    def __init__(self, grafo: Grafo[V, E]):
        self.grafo = grafo
        self.camino: List[V] = []
        self.arbol: Dict[V, Optional[V]] = {}

    @abstractmethod
    def recorrer(self, inicio: V, destino: V) -> None:
        pass

    def reconstruir_camino(self, destino: V) -> List[V]:
        camino = []
        vertice_actual = destino
        while vertice_actual is not None:
            camino.insert(0, vertice_actual)
            vertice_actual = self.arbol.get(vertice_actual)
        return camino

    def hay_camino(self, inicio: V, destino: V) -> bool:
        self.recorrer(inicio, destino)
        return destino in self.arbol

    def camino_hasta(self, inicio: V, destino: V) -> List[V]:
        self.recorrer(inicio, destino)
        return self.reconstruir_camino(destino)

class RecorridoAnchura(Recorrido[V, E]):
    def recorrer(self, inicio: V, destino: V) -> None:
        visitados: Set[V] = set()
        cola = Cola()
        cola.encolar(inicio)
        self.arbol[inicio] = None

        while not cola.esta_vacia():
            vertice = cola.desencolar()

            if vertice == destino:
                break

            if vertice not in visitados:
                visitados.add(vertice)

                for vecino in self.grafo.successors(vertice):
                    if vecino not in visitados:
                        cola.encolar(vecino)
                        if vecino not in self.arbol:
                            self.arbol[vecino] = vertice

        self.camino = self.reconstruir_camino(destino)

class RecorridoProfundidad(Recorrido[V, E]):
    def recorrer(self, inicio: V, destino: V) -> None:
        visitados: Set[V] = set()
        pila = Pila()
        pila.apilar(inicio)
        self.arbol[inicio] = None

        while not pila.esta_vacia():
            vertice = pila.desapilar()

            if vertice == destino:
                break

            if vertice not in visitados:
                visitados.add(vertice)

                for vecino in reversed(list(self.grafo.successors(vertice))):
                    if vecino not in visitados:
                        pila.apilar(vecino)
                        if vecino not in self.arbol:
                            self.arbol[vecino] = vertice

        self.camino = self.reconstruir_camino(destino)

def bfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    recorrido = RecorridoAnchura(grafo)
    return recorrido.camino_hasta(inicio, destino)

def dfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    recorrido = RecorridoProfundidad(grafo)
    return recorrido.camino_hasta(inicio, destino)
