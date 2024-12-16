'''
Created on 21 nov 2024

@author: damat
'''
from __future__ import annotations

from typing import TypeVar, Generic, Dict, Set, Optional, Callable
import matplotlib.pyplot as plt
import networkx as nx

# Definición de tipos genéricos
V = TypeVar('V')  # Tipo para vértices
E = TypeVar('E')  # Tipo para aristas

class Grafo(Generic[V, E]):
    """
    Representaciónde un grafo utilizando un diccionario de adyacencia.
    """
    def __init__(self, es_dirigido: bool = True):
        self.es_dirigido: bool = es_dirigido
        self.adyacencias: Dict[V, Dict[V, E]] = {}  # Diccionario de adyacencia
    
    @staticmethod
    def of(es_dirigido: bool = True) -> Grafo[V, E]:
        return Grafo(es_dirigido)
        """
        Método de factoría para crear un nuevo grafo.
        
        :param es_dirigido: Indica si el grafo es dirigido (True) o no dirigido (False).
        :return: Nuevo grafo.
        """
        
    
    def add_vertex(self, vertice: V) -> None:
        if vertice not in self.adyacencias:
            self.adyacencias[vertice] = {}
        """
        Añade un vértice al grafo si no existe.
        
        :param vertice: Vértice a añadir.
        """
        

    def add_edge(self, origen: V, destino: V, arista: E) -> None:
        self.add_vertex(origen)
        self.add_vertex(destino)
        self.adyacencias[origen][destino] = arista
        if not self.es_dirigido:
            self.adyacencias[destino][origen] = arista
        """
        Añade una arista al grafo entre dos vértices.
        Si el grafo es no dirigido, añade la arista en ambos sentidos.
        
        :param origen: Vértice de origen.
        :param destino: Vértice de destino.
        :param arista: Arista a añadir.
        """

    def successors(self, vertice: V) -> Set[V]:
        return set(self.adyacencias[vertice].keys())
        
        """
        Devuelve los sucesores de un vértice.
        
        :param vertice: Vértice del que se buscan los sucesores.
        :return: Conjunto de sucesores.
        """
        

    def predecessors(self, vertice: V) -> Set[V]:
        return {v for v in self.adyacencias if vertice in self.adyacencias[v]}
        """
        Devuelve los predecesores de un vértice.
        
        :param vertice: Vértice del que se buscan los predecesores.
        :return: Conjunto de predecesores.
        """
        

    def edge_weight(self, origen: V, destino: V) -> Optional[E]:
        return self.adyacencias.get(origen, {}).get(destino)
        """
        Devuelve el peso de la arista entre dos vértices.
        
        :param origen: Vértice de origen.
        :param destino: Vértice de destino.
        :return: Peso de la arista, o None si no existe.
        """
        

    def vertices(self) -> Set[V]:
        return set(self.adyacencias.keys())
    
        """
        Devuelve el conjunto de vértices del grafo.
        
        :return: Conjunto de vértices.
        """
        
    
    def edge_exists(self, origen: V, destino: V) -> bool:
        return destino in self.adyacencias.get(origen, {}).get(destino)
        """
        Verifica si existe una arista entre dos vértices.
        
        :param origen: Vértice de origen.
        :param destino: Vértice de destino.
        :return: True si existe la arista, False en caso contrario.
        """
        

    def subgraph(self, vertices: Set[V]) -> Grafo[V, E]:
        subgrafo = Grafo.of(self.es_dirigido)
        for v in vertices:
            if v in self.adyacencias:
                subgrafo.add_vertex(v)
                for u, arista in self.adyacencias[v].items():
                    if u in vertices:
                        subgrafo.add_edge(v, u, arista)
        return subgrafo 
        """
        Crea un subgraph basado en un conjunto de vértices.
        
        :param vertices: Conjunto de vértices del subgraph.
        :return: Nuevo grafo con los vértices y aristas correspondientes.
        """
        

    def inverse_graph(self) -> Grafo[V, E]:
        if not self.es_dirigido:
            raise ValueError("El grafo inverso solo está definido para grafos dirigidos")
        
        grafo_inverso = Grafo.of(True)
        for origen in self.adyacencias:
            for destino, arista in self.adyacencias[origen].items():
                grafo_inverso.add_edge(destino, origen, arista)
        return grafo_inverso
        """
        Devuelve el grafo inverso (solo válido para grafos dirigidos).
        
        :return: Grafo inverso.
        :raise ValueError: Si el grafo no es dirigido.
        """
        pass

    def draw(self, titulo: str = "Grafo", 
            lambda_vertice: Callable[[V], str] = str, 
            lambda_arista: Callable[[E], str] = str) -> None:
        
        G = nx.DiGraph() if self.es_dirigido else nx.Graph()
    
        for vertice in self.vertices():
            G.add_node(vertice, label=lambda_vertice(vertice))
        for origen in self.vertices():
            for destino, arista in self.adyacencias[origen].items():
                G.add_edge(origen, destino, label=lambda_arista(arista))
    
        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=500, 
                labels=nx.get_node_attributes(G, 'label'))
    
        edge_labels = nx.get_edge_attributes(G, "label")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
        plt.title(titulo)
        plt.show()
        
        

        
    def __str__(self) -> str:
        result = []
        for origen, destinos in self.adyacencias.items():
            destinos_str = ", ".join(f"{destino} ({arista})" for destino, arista in destinos.items())
            result.append(f"{origen} -> {destinos_str}")
        return "\n".join(result)    
        """
        Representación textual del grafo.
        
        Formato libre. Por ejemplo:
            vertice1 -> vertice2 (peso), vertice3 (peso)
            vertice2 -> vertice1 (peso)
            ...
        """
        

if __name__ == '__main__':
    # Crear un grafo dirigido
    grafo = Grafo.of(es_dirigido=True)
    grafo.add_vertex("A")
    grafo.add_vertex("B")
    grafo.add_vertex("C")
    grafo.add_edge("A", "B", 5)
    grafo.add_edge("B", "C", 3)
    
    # Dibujar el grafo
    #grafo.draw(titulo="Mi Grafo Dirigido")
    
    grafo.inverse_graph().draw(titulo="Inverso del Grafo Dirigido")
