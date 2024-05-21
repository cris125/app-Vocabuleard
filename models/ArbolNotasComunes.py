class Nodo:
    def __init__(self, valor) -> None:
        # Inicializa un nodo con el valor proporcionado
        self.suma = 0  # Contador de repeticiones del valor
        self.valor = valor  # Valor del nodo
        self.nodoDerecha = None  # Nodo hijo derecho
        self.nodoIzquierda = None  # Nodo hijo izquierdo

    def __str__(self) -> str:
        # Representación en cadena del nodo, devolviendo su valor
        return str(self.valor)

class ArbolNotasComunes:
    def __init__(self, raiz=None) -> None:
        # Inicializa el árbol, con una raíz opcional
        if raiz is not None:
            self.nodoRaiz = Nodo(raiz)  # Si se proporciona una raíz, crear nodo raíz
        else:
            self.nodoRaiz = None  # Si no, establecer raíz como None

    def es_vacio(self):
        # Comprueba si el árbol está vacío
        return self.nodoRaiz is None

    def insertar(self, valor):
        # Inserta un valor en el árbol
        if self.nodoRaiz is None:
            self.nodoRaiz = Nodo(valor)  # Si el árbol está vacío, crear nodo raíz
        else:
            self.insertarRec(valor, self.nodoRaiz)  # Si no, insertar recursivamente

    def insertarRec(self, valor, nodo):
        # Inserta un valor en el árbol de manera recursiva
        if valor == nodo.valor:
            nodo.suma += 1  # Si el valor es igual al nodo actual, incrementar contador
        elif valor > nodo.valor and nodo.nodoDerecha is None:
            nodo.nodoDerecha = Nodo(valor)  # Si el valor es mayor y no hay hijo derecho, crear nodo hijo derecho
        elif valor < nodo.valor and nodo.nodoIzquierda is None:
            nodo.nodoIzquierda = Nodo(valor)  # Si el valor es menor y no hay hijo izquierdo, crear nodo hijo izquierdo
        elif valor > nodo.valor:
            self.insertarRec(valor, nodo.nodoDerecha)  # Si el valor es mayor, repetir proceso en el hijo derecho
        elif valor < nodo.valor:
            self.insertarRec(valor, nodo.nodoIzquierda)  # Si el valor es menor, repetir proceso en el hijo izquierdo

    def inOrden(self):
        # Realiza un recorrido en orden del árbol y devuelve una lista de valores y sus contadores
        listaInOrden = []  # Lista para almacenar el recorrido en orden

        def inOrdenRecur(nodo):
            if nodo is not None:
                inOrdenRecur(nodo.nodoIzquierda)  # Recorrer hijo izquierdo
                listaInOrden.append({"valor": nodo.valor, "suma": nodo.suma})  # Añadir nodo actual a la lista
                inOrdenRecur(nodo.nodoDerecha)  # Recorrer hijo derecho

        inOrdenRecur(self.nodoRaiz)  # Iniciar el recorrido desde la raíz
        return listaInOrden  # Devolver la lista con el recorrido en orden
