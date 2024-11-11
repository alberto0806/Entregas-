from typing import List, TypeVar, Generic, Callable, Tuple
from abc import ABC, abstractmethod

# Tipos genéricos
E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P')

class Agregado_lineal(ABC, Generic[E]):
    """
    Clase base para los objetos agregados lineales.
    """

    def __init__(self):
        # Inicializa una lista vacía para almacenar elementos
        self._elements: List[E] = []

    def size(self) -> int:
        """
        Devuelve el número de elementos en la colección.
        :return: Int
        """
        return len(self._elements)

    def is_empty(self) -> bool:
        """
        Verifica si la colección está vacía.
        :return: Boolean
        """
        return self.size() == 0

    def elements(self) -> List[E]:
        """
        Devuelve una copia de la lista de elementos.
        :return: List
        """
        return self._elements.copy()
    
    @abstractmethod
    def add(self, e: E) -> None:
        """
        Agrega un elemento a la colección.
        :param e: Elemento a agregar
        :raise NotImplementedError: Método abstracto
        """
        raise NotImplementedError("Método abstracto: debe ser implementado en la subclase.")

    def add_all(self, ls: List[E]) -> None:
        """
        Agrega todos los elementos de una lista a la colección.
        :param ls: Lista a agregar
        :raise NotImplementedError: Método abstracto
        """
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        """
        Remove el primer elemento de la colección.
        :return: Elemento eliminado
        :raise IndexError: Si la colección está vacía
        """
        if self.is_empty():
            raise IndexError("No se puede eliminar de un agregado vacío.")
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        """
        Elimina todos los elementos de la colección.
        :return: Lista eliminada
        """
        removed_elements = self._elements.copy()
        self._elements.clear()
        return removed_elements



class Lista_ordenada(Agregado_lineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        # Inicializa la colección con una función de ordenación
        super().__init__()
        self._order = order

    @classmethod
    def of(cls, order: Callable[[E], R]) -> 'Lista_ordenada[E, R]':
        """
        Crea una instancia de la clase lista ordenada.
        :param order: Función de ordenación
        :return: Instancia de Lista_ordenada
        """
        return cls(order)

    def __index_order(self, e: E) -> int:
        """
        Busca el índice correspondiente a un elemento en la colección.
        :param e: Elemento a buscar
        :return: int
        """
        

    def add(self, e: E) -> None:
        """
        Inserta un elemento en el lugar correspondiente
        :param e: Elemento a agregar
        """
        



class Lista_ordenada_sin_repeticion(Lista_ordenada[E, R], Generic[E, R]):
    def add(self, e: E) -> None:
        """
        Agrega un elemento a la colección sin repetición.
        :param e: Elemento a agregar
        :raise NotImplementedError: Método abstracto
        """
        



class Cola(Agregado_lineal[E]):
    @classmethod
    def of(cls) -> 'Cola[E]':
        # Crea una cola vacía
        

    def add(self, e: E) -> None:
        """
        Agrega un elemento a la cola.
        :param e: Elemento a agregar
        :raise NotImplementedError: Método abstracto
        """
        



class Cola_prioridad(Generic[E, P]):
    def __init__(self):
        # Inicializa dos listas vacías, una para los elementos y otra para sus prioridades
        

    def size(self) -> int:
        """
        Devuelve el número de elementos en la cola.
        :return: Int
        """
        

    def is_empty(self) -> bool:
        """
        Verifica si la cola está vacía.
        :return: Boolean
        """
        

    def elements(self) -> List[E]:
        """
        Devuelve una copia de la lista de elementos de mayor a menor prioridad
        :return: List
        """
        

    def add(self, e: E, priority: P) -> None:
        """
        Agrega un elemento y sus prioridades a la cola.
        :param e: Elemento a agregar
        :param priority: Prioridad del elemento
        """
        

    def remove(self) -> E:
        """
        Elimina el primer elemento de la cola. El primer elemento es el de mayor prioridad.
        :return: Elemento eliminado
        :raise IndexError: Si la cola está vacía
        """
        

    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        """
        Agrega todos los elementos y sus prioridades a la cola.
        :param ls: Lista de tuplas (elemento, prioridad)
        """
        

    def decrease_priority(self, e: E, new_priority: P) -> None:
        """
        Reduce la prioridad del elemento en la cola. El elemento debe estar en la cola, y la nueva prioridad debe ser menor
        :param e: Elemento a reducir prioridad.
        :param new_priority: Prioridad nueva para el elemento
        """
        



class Pila(Agregado_lineal[E]):
    """
    Una Pila es una estructura de datos que sigue el principio LIFO (Last In, First Out).
    Los elementos se apilan y solo se puede acceder al elemento en la parte superior.
    
    IMPORTANTE. Como la estructura subyacente es una lista, la parte superior de la pila es el primer 
    elemento de la lista.
    """

    