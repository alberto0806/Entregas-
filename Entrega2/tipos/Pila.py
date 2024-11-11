'''
Created on 2 nov 2024

@author: alber
'''
from __future__ import annotations
from tipos.Agregado_lineal import Agregado_lineal
from typing import TypeVar

E = TypeVar('E')

class Pila(Agregado_lineal[E]):
    @staticmethod
    def of() -> Pila[E]:
        return Pila()

    def add(self, e: E) -> None:
        self._elements.insert(0, e)

    def __str__(self):
        return f"Pila({self._elements})"