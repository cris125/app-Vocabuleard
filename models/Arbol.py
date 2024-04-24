class Nodo:
    def __init__(self,valor) -> None:
        self.valor=valor
        self.nodoDerecha=None
        self.nodoIzquierda=None
    def __str__(self) -> str:
        return self.valor
    
class Arbol():
    def __init__(self, raiz=None) -> None:
        if raiz!=None:
            self.nodoRaiz = Nodo(6)
        else:
            self.nodoRaiz = Nodo(6)
            
    def es_vacio(self):
        return self.nodoRaiz is None
    
    def insertar(self, valor):
        if self.nodoRaiz==None:
            self.nodoRaiz=Nodo(valor)
        else:
            self.insertarRec(valor, self.nodoRaiz)

    def insertarRec(self, valor, nodo):
        if valor >= nodo.valor and nodo.nodoDerecha is None:
            nodo.nodoDerecha = Nodo(valor)
        elif valor < nodo.valor and nodo.nodoIzquierda is None:
            nodo.nodoIzquierda = Nodo(valor)
        elif valor >= nodo.valor:
            self.insertarRec(valor, nodo.nodoDerecha)
        elif valor < nodo.valor:
            self.insertarRec(valor, nodo.nodoIzquierda)

    def bus(self, valor):
        return self.busca(self.nodoRaiz, valor)

    def busca(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == valor:
            return True
        elif valor < nodo_actual.valor:
            return self.busca(nodo_actual.nodoIzquierda, valor)
        else:
            return self.busca(nodo_actual.nodoDerecha, valor)

    def preOrden(self):
        def preOrdenRecur(nodo):
            if nodo!= None:
                print(nodo.valor,end=" ")
                preOrdenRecur(nodo.nodoIzquierda)
                preOrdenRecur(nodo.nodoDerecha)
        preOrdenRecur(self.nodoRaiz)        
    
    def inOrden(self):
        def inOrdenRecur(nodo):
            if nodo!= None:
                
                inOrdenRecur(nodo.nodoIzquierda)
                print(nodo.valor,end=" ")
                inOrdenRecur(nodo.nodoDerecha)
        inOrdenRecur(self.nodoRaiz)    

    def posOrden(self):
        def posOrdenRecur(nodo):
            if nodo!= None:
                
                posOrdenRecur(nodo.nodoIzquierda)
                posOrdenRecur(nodo.nodoDerecha)
                print(nodo.valor,end=" ")
        posOrdenRecur(self.nodoRaiz) 
    
    def hallarAltura(nodo):
        altura=[0] 
        def alturaRecur(nodo,alturaNodo):
            if nodo != None:
                alturaRecur(nodo.nodoDerecha,alturaNodo+1)
                alturaRecur(nodo.nodoIzquierda,alturaNodo+1)
                if  altura[0]<alturaNodo:
                    altura[0]=alturaNodo    
        alturaRecur(nodo,0)
        return(altura[0]+1)
    
    
    def imprimirArbol(self):
        lista=[]
        
        def hacerMatrizArbol(A):
                    hacerMatrizArbol_rec(A, 0)
        def hacerMatrizArbol_rec( nodo, profundidad):
                if nodo is not None:
                    hacerMatrizArbol_rec(nodo.nodoIzquierda, profundidad + 1)
                    are=[]
                    for i in range(profundidad):
                            are.append("")
                    are.append("("+str(nodo.valor)+")")
                    lista.append(are)
                    hacerMatrizArbol_rec(nodo.nodoDerecha, profundidad + 1)

        def arreglarMatriz():
            num=0
            for i in lista:
                if len(i)>num:
                    num=len(i)
            for i in range(len(lista)):
                while len(lista[i]) != num:
                    lista[i].append("")
            return [list(row) for row in zip(*lista)]
        

        def agregarLineasEimprimir(matriz_transpuesta):
            y=[]
            for i in range(len(matriz_transpuesta)):
                f=matriz_transpuesta[i].copy()
                y.append(f.copy())
                for x in range(len(matriz_transpuesta[i])):
                    if matriz_transpuesta[i][x] !="":
                            f[x-1]="    "
                            f[x]="/ \\"
                y.append(f)

            for fila in y:
                print("\n")
                for i in fila:
                    if i == "":
                        print("    ",end="")
                    else:
                        print(i,end="")

        hacerMatrizArbol(self.nodoRaiz)
        matriz_transpuesta =arreglarMatriz() 
        agregarLineasEimprimir(matriz_transpuesta)
        print("\n")

    
    
    def eliminar(self, valor):
        self.nodoRaiz = self.eliminarRec(self.nodoRaiz, valor)

    def eliminarRec(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.nodoIzquierda = self.eliminarRec(nodo.nodoIzquierda, valor)
        elif valor > nodo.valor:
            nodo.nodoDerecha = self.eliminarRec(nodo.nodoDerecha, valor)
        else:
            # Caso 1: Nodo sin hijos o con un solo hijo
            if nodo.nodoIzquierda is None:
                temp = nodo.nodoDerecha
                nodo = None
                return temp
            elif nodo.nodoDerecha is None:
                temp = nodo.nodoIzquierda
                nodo = None
                return temp

            # Caso 2: Nodo con dos hijos, se obtiene el sucesor inorder
            temp = self.minValorNodo(nodo.nodoDerecha)
            nodo.valor = temp.valor
            nodo.nodoDerecha = self.eliminarRec(nodo.nodoDerecha, temp.valor)

        return nodo

    def minValorNodo(self, node):
        minVal = node
        while minVal.nodoIzquierda is not None:
            minVal = minVal.nodoIzquierda
        return minVal
    
    def verMatriz(self):
        lista=[]
        
        def hacerMatrizArbol(A):
                    hacerMatrizArbol_rec(A, 0)
        def hacerMatrizArbol_rec( nodo, profundidad):
                if nodo is not None:
                    hacerMatrizArbol_rec(nodo.nodoIzquierda, profundidad + 1)
                    are=[]
                    for i in range(profundidad):
                            are.append("")
                    are.append("("+str(nodo.valor)+")")
                    lista.append(are)
                    hacerMatrizArbol_rec(nodo.nodoDerecha, profundidad + 1)

        def arreglarMatriz():
            num=0
            for i in lista:
                if len(i)>num:
                    num=len(i)
            for i in range(len(lista)):
                while len(lista[i]) != num:
                    lista[i].append("")
            return [list(row) for row in zip(*lista)]
        

        def agregarLineas(matriz_transpuesta):
            for i in range(len(matriz_transpuesta)):
                for x in range(len(matriz_transpuesta[i])):
                    if matriz_transpuesta[i][x] !="":
                            matriz_transpuesta[i][x]=matriz_transpuesta[i][x]+"\n"+"/   \\"
            return(matriz_transpuesta)

        hacerMatrizArbol(self.nodoRaiz)
        matriz_transpuesta =arreglarMatriz() 
        return agregarLineas(matriz_transpuesta)

