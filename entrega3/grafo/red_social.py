from __future__ import annotations

from dataclasses import dataclass
from typing import Dict
from datetime import date, datetime
from grafo.recorridos import *
from grafo.grafo1 import *
import re 
        
@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date

    def __post_init__(self):
        if not re.match(r'^\d{8}[A-Z]$', self.dni):
            raise ValueError("DNI debe tener 8 dígitos seguidos de una letra mayúscula")
        if self.fecha_nacimiento >= date.today():
            raise ValueError("La fecha de nacimiento debe ser anterior a la fecha actual")

    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> Usuario:
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)

    @staticmethod
    def parse(texto: str) -> Usuario:
        dni, nombre, apellidos, fecha_str = texto.split(',')
        fecha_nacimiento = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)

    def __str__(self) -> str:
        return f"{self.dni} - {self.nombre}"

@dataclass(frozen=True)
class Relacion:
    id: int
    interacciones: int
    dias_activa: int
    __n: int = 0  # Contador de relaciones

    @staticmethod
    def of(interacciones: int, dias_activa: int) -> Relacion:
        Relacion.__n += 1
        return Relacion(Relacion.__n, interacciones, dias_activa)

    def __str__(self) -> str:
        return f"({self.id} - días activa: {self.dias_activa} - num interacciones {self.interacciones})"

class Red_social(Grafo[Usuario, Relacion]):
    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        self.usuarios_dni: Dict[str, Usuario] = {}

    @staticmethod
    def of(es_dirigido: bool = False) -> Red_social:
        return Red_social(es_dirigido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> Red_social:
        red = Red_social(es_dirigido)

        # Leer usuarios
        with open(f1, 'r', encoding='utf-8') as file:
            for line in file:
                usuario = Usuario.parse(line.strip())
                red.add_vertex(usuario)
                red.usuarios_dni[usuario.dni] = usuario

        # Leer relaciones
        with open(f2, 'r', encoding='utf-8') as file:
            for line in file:
                dni1, dni2, interacciones, dias_activa = line.strip().split(',')
                usuario1 = red.usuarios_dni[dni1]
                usuario2 = red.usuarios_dni[dni2]
                relacion = Relacion.of(int(interacciones), int(dias_activa))
                red.add_edge(usuario1, usuario2, relacion)

        return red

    def __str__(self) -> str:
        return f"Red social con {len(self.vertices())} usuarios y {sum(len(edges) for edges in self.adyacencias.values())} relaciones"

if __name__ == '__main__':
    raiz = '../../' # Cambia esta variable si ejecutas este script desde otro directorio
    rrss = Red_social.parse(raiz+'resources/usuarios.txt', raiz+'resources/relaciones.txt', es_dirigido=False)

    print("El camino más corto desde 25143909I hasta 87345530M es:")
    camino = bfs(rrss, rrss.usuarios_dni['25143909I'], rrss.usuarios_dni['87345530M'])
    g_camino = rrss.subgraph(camino)

    g_camino.draw("caminos", lambda_vertice=lambda v: f"{v.dni}", lambda_arista=lambda e: e.id)
