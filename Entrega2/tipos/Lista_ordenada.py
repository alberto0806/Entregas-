'''
Created on 2 nov 2024

@author: alber
'''
from __future__ import annotations
from typing import Generic, TypeVar, Callable, List
from tipos.Agregado_lineal import Agregado_lineal

E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada(Agregado_lineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self.__order = order

    @classmethod
    def of(cls, order: Callable[[E], R]) -> Lista_ordenada[E, R]:
        return cls(order)

    def __index_order(self, e: E) -> int:
        for i, elem in enumerate(self._elements):
            if self.__order(e) <= self.__order(elem):
                return i
        return len(self._elements)

    def add(self, e: E) -> None:
        index = self.__index_order(e)
        self._elements.insert(index, e)

    def __str__(self):
        return f"ListaOrdenada({self._elements})"


            
        
        
        
