class BTreeNode:
    def __init__(self, t, leaf=True):
        self.t = t
        self.keys = []
        self.values = []  # Lista para almacenar los significados
        self.children = []
        self.leaf = leaf

class BTreeDictionary:
    def __init__(self, t):
        self.root = BTreeNode(t)
        self.t = t

    def search(self, key, node=None):
        if node is None:
            node = self.root
        i = 0
        try:
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            if i < len(node.keys) and key == node.keys[i]:
                return node.keys[i], node.values[i]
            elif not node.leaf:
                return self.search(key, node.children[i])
            else:
                return None
        except:
            return None 

    def insert(self, key, value, node=None):
        if node is None:
            node = self.root
        if len(node.keys) == (2 * self.t) - 1:
            new_node = BTreeNode(self.t, leaf=False)
            new_node.children.append(node)
            self.split(new_node, 0)
            self.root = new_node
            self.insert_non_full(new_node, key, value)
        else:
            self.insert_non_full(node, key, value)

    def insert_non_full(self, node, key, value):
        i = len(node.keys) - 1
        while i >= 0 and key < node.keys[i]:
            i -= 1
        i += 1
        if node.leaf:
            node.keys.insert(i, key)
            node.values.insert(i, value)
        else:
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key, value)

    def split(self, node, i):
        t = self.t
        child = node.children[i]
        new_child = BTreeNode(t, leaf=child.leaf)
        node.keys.insert(i, child.keys[t - 1])
        node.values.insert(i, child.values[t - 1])
        node.children.insert(i + 1, new_child)
        new_child.keys = child.keys[t:]
        new_child.values = child.values[t:]
        child.keys = child.keys[:t - 1]
        child.values = child.values[:t - 1]


class Diccionario():
    def hacerDiccionario(self):
        dictionary = BTreeDictionary(11)

        words_definitions = {
            # Inglés a Español
            "hello": "hola", "goodbye": "adiós", "cat": "gato", "dog": "perro", "tree": "árbol", "car": "coche",
            "house": "casa", "book": "libro", "computer": "computadora", "keyboard": "teclado", "mouse": "ratón",
            "phone": "teléfono", "television": "televisión", "chair": "silla", "table": "mesa", "pen": "pluma",
            "pencil": "lápiz", "student": "estudiante", "teacher": "profesor", "school": "escuela", "university": "universidad",
            "hospital": "hospital", "doctor": "doctor", "nurse": "enfermera", "medicine": "medicina", "bank": "banco",
            "money": "dinero", "wallet": "cartera", "credit card": "tarjeta de crédito", "restaurant": "restaurante",
            "food": "comida", "drink": "bebida", "coffee": "café", "tea": "té", "water": "agua", "juice": "jugo",
            "bread": "pan", "fruit": "fruta", "vegetable": "verdura", "pizza": "pizza", "hamburger": "hamburguesa",
            "fries": "papas fritas", "ice cream": "helado",

            "hola": "hello", "adiós": "goodbye", "gato": "cat", "perro": "dog", "árbol": "tree", "coche": "car",
            "casa": "house", "libro": "book", "computadora": "computer", "teclado": "keyboard", "ratón": "mouse",
            "teléfono": "phone", "televisión": "television", "silla": "chair", "mesa": "table", "pluma": "pen",
            "lápiz": "pencil", "estudiante": "student", "profesor": "teacher", "escuela": "school", "universidad": "university",
            "hospital": "hospital", "doctor": "doctor", "enfermera": "nurse", "medicina": "medicine", "banco": "bank",
            "dinero": "money", "cartera": "wallet", "tarjeta de crédito": "credit card", "restaurante": "restaurant",
            "comida": "food", "bebida": "drink", "café": "coffee", "té": "tea", "agua": "water", "jugo": "juice",
            "pan": "bread", "fruta": "fruit", "verdura": "vegetable", "pizza": "pizza", "hamburguesa": "hamburger",
            "papas fritas": "fries", "helado": "ice cream",

            "apple": "manzana", "orange": "naranja", "banana": "plátano", "grape": "uva", "lemon": "limón",
            "melon": "melón", "peach": "durazno", "pear": "pera", "pineapple": "piña", "strawberry": "fresa",
            "watermelon": "sandía", "blueberry": "arándano", "cherry": "cereza", "apricot": "albaricoque", "kiwi": "kiwi",
            "mango": "mango", "papaya": "papaya", "pomegranate": "granada", "raspberry": "frambuesa", "blackberry": "zarzamora",
            "lime": "lima", "avocado": "aguacate", "fig": "higo", "coconut": "coco", "cranberry": "arándano rojo",
            "guava": "guayaba", "date": "dátil", "passion fruit": "maracuyá", "starfruit": "carambola", "tangerine": "mandarina",
            "persimmon": "caqui", "nectarine": "nectarina", "dragon fruit": "pitahaya", "lychee": "lichí", "quince": "membrillo",
            "plum": "ciruela", "mulberry": "mora", "elderberry": "saúco", "boysenberry": "zarzamora de Boysen", "soursop": "guanábana",
            "tamarind": "tamarindo", "jabuticaba": "jaboticaba", "jackfruit": "yaca", "rhubarb": "ruibarbo", "kumquat": "kumquat",
            "breadfruit": "fruta del pan", "sapodilla": "zapote", "persimmon": "caqui", "plantain": "plátano macho", "durian": "durián",
            "cantaloupe": "melón cantalupo", "horned melon": "pepino cornudo", "feijoa": "feijoa", "acai berry": "baya de acai",
            "mangosteen": "mangostán", "rambutan": "rambután", "custard apple": "chirimoya", "soursop": "guanábana", "guava": "guayaba",
            "tamarillo": "tamarillo", "ugli fruit": "ugli", "yuzu": "yuzu", "passionfruit": "maracuyá", "kiwifruit": "kiwi",
            "star apple": "caimito", "horned melon": "pepino cornudo", "carambola": "carambola", "dragon fruit": "pitahaya",
        }


        for word, definition in words_definitions.items():
            dictionary.insert(word, definition)

        return(dictionary)