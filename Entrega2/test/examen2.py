'''
Created on 21 nov 2024

@author: alber
'''
from typing import Generic, TypeVar, Callable, List
from abc import ABC, abstractmethod

E = TypeVar('E')

class Agregado_lineal(ABC, Generic[E]):
    def __init__(self):
        self._elementos: List[E] = []

    @property
    def size(self) -> int:
        return len(self._elementos)

    @property
    def is_empty(self) -> bool:
        return len(self._elementos) == 0

    @property
    def elements(self) -> List[E]:
        return self._elementos.copy()

    @abstractmethod
    def add(self, e: E) -> None:
        pass

    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        if self.is_empty:
            raise IndexError('El agregado está vacío')
        return self._elementos.pop(0)

    def remove_all(self) -> List[E]:
        removed = self._elementos.copy()
        self._elementos.clear()
        return removed

    def contains(self, e: E) -> bool:
        return e in self._elementos

    def find(self, func: Callable[[E], bool]) -> E | None:
        for elemento in self._elementos:
            if func(elemento):
                return elemento
        return None

    def filter(self, func: Callable[[E], bool]) -> List[E]:
        return [elemento for elemento in self._elementos if func(elemento)]


class ColaConLimite(Agregado_lineal[E]):
    def __init__(self, capacidad: int):
        super().__init__()
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser un número positivo")
        self._capacidad = capacidad

    @classmethod
    def of(cls, capacidad: int):
        return cls(capacidad)

    def add(self, e: E) -> None:
        if self.is_full():
            raise OverflowError("La cola está llena.")
        self._elementos.append(e)

    def is_full(self) -> bool:
        return len(self._elementos) == self._capacidad

    @property
    def capacidad(self) -> int:
        return self._capacidad


if __name__ == "__main__":
    print("=== Pruebas de ColaConLimite ===")
    cola = ColaConLimite.of(3)

    print("Prueba agregar y eliminar:")
    cola.add(1)
    cola.add(2)
    cola.add(3)
    print(cola.remove())  # Esperado: 1
    print(cola.remove())  # Esperado: 2
    print(cola.remove())  # Esperado: 3
    try:
        cola.remove()
    except IndexError as e:
        print(e)  # Esperado: El agregado está vacío

    print("\nPrueba de is_empty:")
    print(cola.is_empty)  # Esperado: True
    cola.add(4)
    print(cola.is_empty)  # Esperado: False

    print("\nPrueba de contains:")
    cola.add(5)
    print(cola.contains(4))  # Esperado: True
    print(cola.contains(6))  # Esperado: False

    print("\nPrueba de find:")
    es_par = lambda x: x % 2 == 0
    print(cola.find(es_par))  # Esperado: 4
    print(cola.find(lambda x: x > 10))  # Esperado: None

    print("\nPrueba de filter:")
    mayores_que_cuatro = lambda x: x > 4
    print(cola.filter(mayores_que_cuatro))  # Esperado: [5]

    print("\nPrueba de is_full:")
    cola.add(6)
    print(cola.is_full())  # Esperado: True

    print("\nPrueba de excepción por sobrecarga:")
    try:
        cola.add(7)
    except OverflowError as e:
        print(e)  # Esperado: La cola está llena.

    print("\nPrueba de método de factoría:")
    nueva_cola = ColaConLimite.of(2)
    print(nueva_cola.capacidad)  # Esperado: 2
    print(nueva_cola.is_full())  # Esperado: False


