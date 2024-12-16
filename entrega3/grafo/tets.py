'''
Created on 16 dic 2024

@author: alber
'''
from grafo.grafo1 import Grafo
from grafo.red_social import *
# Assuming the Usuario, Relacion, and Red_social classes are defined as provided

def test_grafo():
    grafo = Grafo.of(es_dirigido=False)
    usuarios = {
        "18909774Z": Usuario("18909774Z", "Maria", "Diaz", date(1995, 1, 5)),
        "95287188O": Usuario("95287188O", "Pedro", "Garcia", date(1990, 5, 15)),
        "55039956S": Usuario("55039956S", "David", "Lopez", date(1985, 8, 20)),
        "60412985S": Usuario("60412985S", "Maria", "Rodriguez", date(1992, 3, 10)),
        "95157732O": Usuario("95157732O", "Pedro", "Martinez", date(1988, 11, 25)),
        "58127458W": Usuario("58127458W", "Maria", "Sanchez", date(1993, 7, 8)),
        "56427434U": Usuario("56427434U", "Elena", "Fernandez", date(1991, 9, 30)),
        "71894470A": Usuario("71894470A", "Carlos", "Gomez", date(1987, 4, 12)),
        "25143909I": Usuario("25143909I", "Lucia", "Lopez", date(1994, 6, 18)),
        "45718832U": Usuario("45718832U", "Carlos", "Ruiz", date(1989, 2, 7)),
        "82007713N": Usuario("82007713N", "Carlos", "Hernandez", date(1986, 10, 15)),
        "16274768S": Usuario("16274768S", "Juan", "Jimenez", date(1992, 12, 3)),
        "76929765H": Usuario("76929765H", "Juan", "Alvarez", date(1990, 8, 22)),
        "63506915L": Usuario("63506915L", "Lucia", "Moreno", date(1993, 5, 9)),
        "62258675I": Usuario("62258675I", "Laura", "Muñoz", date(1988, 1, 28)),
        "92322186A": Usuario("92322186A", "Pedro", "Alonso", date(1991, 7, 14)),
        "85707754E": Usuario("85707754E", "Jorge", "Gutierrez", date(1987, 11, 6)),
        "61832964Y": Usuario("61832964Y", "Pedro", "Romero", date(1994, 3, 19)),
        "10115245D": Usuario("10115245D", "Ana", "Navarro", date(1989, 9, 2)),
        "87345530M": Usuario("87345530M", "Ana", "Rodriguez", date(1992, 4, 25))
    }

    for usuario in usuarios.values():
        grafo.add_vertex(usuario)

    # Agregar algunas relaciones de ejemplo
    grafo.add_edge(usuarios["18909774Z"], usuarios["95287188O"], Relacion.of(10, 30))
    grafo.add_edge(usuarios["18909774Z"], usuarios["55039956S"], Relacion.of(15, 45))
    grafo.add_edge(usuarios["25143909I"], usuarios["45718832U"], Relacion.of(20, 60))
    grafo.add_edge(usuarios["25143909I"], usuarios["87345530M"], Relacion.of(25, 75))
    grafo.add_edge(usuarios["45718832U"], usuarios["82007713N"], Relacion.of(30, 90))

    print("************** Nº Predecesores de cada vértice")
    for usuario in usuarios.values():
        print(f"{usuario} -- {len(grafo.predecessors(usuario))}")

    print("\n************** Nº Vecinos de cada vértice")
    for usuario in usuarios.values():
        print(f"{usuario} -- {len(grafo.successors(usuario))}")

def test_recorrido_en_anchura():
    grafo = Grafo[Usuario, Relacion]()
    raiz = '../../' # Cambia esta variable si ejecutas este script desde otro directorio
    rrss = Red_social.parse(raiz+'resources/usuarios.txt', raiz+'resources/relaciones.txt', es_dirigido=False)

    inicio = usuarios["25143909I"]
    fin = usuarios["87345530M"]
    recorrido = RecorridoAnchura(grafo)
    recorrido.recorrer(inicio, fin)

    print("El camino más corto desde 25143909I hasta 87345530M es:")
    print(recorrido.camino)
    print(f"La distancia mínima es: {len(recorrido.camino) - 1} pasos.")

def test_recorrido_en_profundidad():
    grafo = Grafo[Usuario, Relacion]()
    # ... (agregar usuarios y relaciones como en test_grafo)

    inicio = usuarios["25143909I"]
    fin = usuarios["76929765H"]
    recorrido = RecorridoProfundidad(grafo)
    recorrido.recorrer(inicio, fin)

    if not recorrido.camino:
        print("No hay conexión directa entre 25143909I y 76929765H.")
    else:
        print("Hay conexión directa entre 25143909I y 76929765H.")

if __name__ == "__main__":
    test_grafo()
    test_recorrido_en_anchura()
    test_recorrido_en_profundidad()






