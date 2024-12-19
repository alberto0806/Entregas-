'''
Created on 19 dic 2024

@author: alber
'''
import networkx as nx
import matplotlib.pyplot as plt

class Gen:
    def __init__(self, nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str):
        self._nombre = nombre
        self._tipo = tipo
        self._num_mutaciones = max(0, num_mutaciones)
        self._loc_cromosoma = loc_cromosoma

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def num_mutaciones(self) -> int:
        return self._num_mutaciones

    @property
    def loc_cromosoma(self) -> str:
        return self._loc_cromosoma

    @classmethod
    def parse(cls, line: str) -> 'Gen':
        parts = [part.strip() for part in line.split(',')]
        if len(parts) != 4:
            raise ValueError(f"Invalid line format: {line}")
        nombre, tipo, num_mutaciones, loc_cromosoma = parts
        try:
            num_mutaciones = int(num_mutaciones)
        except ValueError:
            print(f"Warning: Invalid number of mutations '{num_mutaciones}' for gene '{nombre}'. Setting to 0.")
            num_mutaciones = 0
        return cls(nombre, tipo, num_mutaciones, loc_cromosoma)

class RedGenica:
    def __init__(self, es_dirigido: bool = False):
        self.graph = nx.DiGraph() if es_dirigido else nx.Graph()
        self.genes_por_nombre = {}

    def add_vertice(self, gen: Gen):
        self.graph.add_node(gen.nombre, gen=gen)

    def add_arista(self, gen1: Gen, gen2: Gen, relacion: float):
        self.graph.add_edge(gen1.nombre, gen2.nombre, weight=relacion)

    @classmethod
    def parse(cls, f1: str, f2: str, es_dirigido: bool = False) -> 'RedGenica':
        red = cls(es_dirigido)
        red._leer_genes(f1)
        red._leer_relaciones(f2)
        return red

    def _leer_genes(self, fichero_genes: str) -> None:
        with open(fichero_genes, 'r') as f:
            for linea in f:
                if linea.strip():
                    gen = Gen.parse(linea)
                    self.genes_por_nombre[gen.nombre] = gen
                    self.add_vertice(gen)

    def _leer_relaciones(self, fichero_relaciones: str) -> None:
        with open(fichero_relaciones, 'r') as f:
            for linea in f:
                if linea.strip():
                    gen1_nombre, gen2_nombre, conexion = map(str.strip, linea.split(','))
                    gen1 = self.genes_por_nombre[gen1_nombre]
                    gen2 = self.genes_por_nombre[gen2_nombre]
                    self.add_arista(gen1, gen2, float(conexion))

    def recorrido_profundidad(self, inicio: str, fin: str) -> list:
        try:
            
            path = nx.shortest_path(self.graph, inicio, fin)
            return path
        except nx.NetworkXNoPath:
            return []

    def crear_subgrafo(self, nodos: list) -> nx.Graph:
        return self.graph.subgraph(nodos)

    def dibujar_grafo(self, grafo: nx.Graph):
        plt.figure(figsize=(6, 10))  
        
       
        pos = {}
        nodes = list(grafo.nodes())
        for i, node in enumerate(nodes):
            pos[node] = (0, -i)  # Align nodes vertically
        
        
        nx.draw_networkx_nodes(grafo, pos, 
                             node_color='lightblue',
                             node_size=1000)
        
        
        nx.draw_networkx_edges(grafo, pos)
        
        
        nx.draw_networkx_labels(grafo, pos)
        
       
        edge_labels = nx.get_edge_attributes(grafo, 'weight')
        nx.draw_networkx_edge_labels(grafo, pos, edge_labels)
        
        plt.axis('off')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
   
    raiz = '../../' 
    red_genica = RedGenica.parse(raiz+'resources/genes.txt', raiz+'resources/red_genes.txt', es_dirigido=False)
    
    camino = red_genica.recorrido_profundidad('KRAS', 'PIK3CA')
    print("Path found:", ' -> '.join(camino))
    
    # 3. Create and draw subgraph
    subgrafo = red_genica.crear_subgrafo(camino)
    red_genica.dibujar_grafo(subgrafo)
    
