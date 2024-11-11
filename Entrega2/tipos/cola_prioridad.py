'''
Created on 2 nov 2024

@author: alber
'''


from typing import List, TypeVar, Generic, Callable, Tuple
from abc import ABC, abstractmethod

# Tipos genéricos
E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P')
class Cola_prioridad(Generic[E, P]):
    def __init__(self):
        # Inicializa dos listas vacías, una para los elementos y otra para sus prioridades
        self._elements: List[E] = []
        self._priorities: List[P] = []
    
    @property
    def size(self) -> int:
        return len(self._elements)
        
        

    def is_empty(self) -> bool:
       
        return len(self._elements) == 0

    def elements(self) -> List[E]:
        
        return self._elements.copy()
        

    def add(self, e: E, priority: P) -> None:
        
        index = self.index_order(priority)
        self._elements.insert(index, e)
        self._priorities.insert(index, priority)

    def remove(self) -> E:
        
        assert len(self._elements) > 0, 'El agregado está vacío'
        self._priorities.pop(0)
        return self._elements.pop(0)

    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        for e, p in ls:
            self.add(e, p)
    
    def remove_all(self) -> List[E]:
        removed = []
        while not self.is_empty:
            removed.append(self.remove())
        return removed
    
    
    def index_order(self, priority: P) -> int:
        for i, p in enumerate(self._priorities):
            if priority < p:
                return i
        return len(self._priorities)
    
    
    
    def decrease_priority(self, e: E, new_priority: P) -> None:
        if e in self._elements:
            index = self._elements.index(e)
            old_priority = self._priorities[index]
            if new_priority < old_priority:
                self._elements.pop(index)
                self._priorities.pop(index)
                self.add(e, new_priority)
                
    def __str__(self):
        return f"ColaPrioridad({list(zip(self._elements, self._priorities))})"