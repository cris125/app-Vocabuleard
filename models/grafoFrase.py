import random
class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, frase):
        if frase[0] not in self.nodos:
            self.nodos[frase[0]] = set()

    def agregar_relacion(self, frase1, frase2):
        self.agregar_nodo(frase1)
        self.agregar_nodo(frase2)
        self.nodos[frase1[0]].add(frase2[0])
        
    def obtener_relaciones(self, frase):
        if frase[0] in self.nodos:
            return self.nodos[frase[0]]
        else:
            return set()

class Interfaz:
    def __init__(self,grafo):
        self.grafo = grafo

    def agregar_frase(self, frase):
        self.grafo.agregar_nodo(frase)

    def agregar_relaciones_columnas(self, columnas):
        for i in range(len(columnas) - 1):
            for frase1 in columnas[i]:
                for frase2 in columnas[i+1]:
                    self.grafo.agregar_relacion(frase1, frase2)

    def obtener_relaciones(self, frase):
        return (self.grafo.obtener_relaciones(frase))


class FraseGrafo():
    columnas = [
        [ ["The sun shines", "El sol brilla"], ["Children laugh", "Los niños ríen"], ["Mountains rise", "Las montañas se levantan"], ["Love abounds", "El amor abunda"], ["Time passes", "El tiempo pasa"] ],
        [ ["Birds chirp", "Los pájaros gorjean"], ["Bells ring", "Las campanas suenan"], ["Oceans roar", "Los océanos rugen"], ["Hope remains", "La esperanza permanece"], ["Seasons change", "Las estaciones cambian"] ],
        [ ["Flowers bloom", "Las flores florecen"], ["Waves crash", "Las olas chocan"], ["Cities bustle", "Las ciudades bulliciosas"], ["Joy resounds", "La alegría resuena"], ["Memories linger", "Los recuerdos persisten"] ],
        [ ["Rivers flow", "Los ríos fluyen"], ["Raindrops fall", "Las gotas de lluvia caen"], ["Forests whisper", "Los bosques susurran"], ["Peace prevails", "La paz prevalece"], ["Moments cherish", "Los momentos atesoran"] ],
        [ ["Breezes blow", "Las brisas soplan"], ["Fires crackle", "Los fuegos crepitan"], ["Deserts shimmer", "Los desiertos brillan"], ["Faith endures", "La fe perdura"], ["Opportunities arise", "Las oportunidades surgen"] ],
        [ ["Leaves rustle", "Las hojas susurran"], ["Snowflakes dance", "Los copos de nieve bailan"], ["Skies shimmer", "Los cielos brillan"], ["Dreams inspire", "Los sueños inspiran"], ["Possibilities unfold", "Las posibilidades se despliegan"] ],
        [ ["Stars twinkle", "Las estrellas parpadean"], ["Hearts flutter", "Los corazones palpitan"], ["Dreams ignite", "Los sueños se encienden"], ["Courage soars", "El coraje se eleva"], ["Dreams awaken", "Los sueños despiertan"] ]
    ]
    def hacerFrase(self):
        palabra=[]
        for i in range(len(self.columnas)):
            palabra.append(self.columnas[i][random.randrange(5)])
        return(palabra)
    
    def hacerGrafo(self):
        grafo=Grafo()
        interfaz = Interfaz(grafo)
        
        for columna in self.columnas:
            for frase in columna:
                interfaz.agregar_frase(frase)
        
        interfaz.agregar_relaciones_columnas(self.columnas)
        
        relaciones = interfaz.obtener_relaciones(["The sun shines", ""])
        print("Relaciones de 'Birds chirp' ('El sol brilla):", relaciones)
        return(interfaz)
    