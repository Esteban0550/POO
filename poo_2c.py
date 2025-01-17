class Personaje:
    # Constructor con doble guión bajo (__init__)
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    # Método para imprimir atributos
    def imprimir_atributos(self):
        print(self.nombre)
        print("- Fuerza:", self.fuerza)
        print("- Inteligencia:", self.inteligencia)
        print("- Defensa:", self.defensa)
        print("- Vida:", self.vida)

    # Método para subir nivel
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    # Método para verificar si está vivo
    def esta_vivo(self):
        return self.vida > 0

    # Método para simular la muerte
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    # Método para calcular el daño infligido
    def dañar(self, enemigo):
        daño = self.fuerza - enemigo.defensa
        return max(daño, 0)

    # Método para atacar a un enemigo
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("Vida de", enemigo.nombre, "es", enemigo.vida)

# Clase Guerrero que hereda de Personaje
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("- Espada:", self.espada)

    def dañar(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

    def escoger_Navaja(self):
        opcion = int(input("Escoge tu fierro:\n(1) Navaja suiza, Daño 10.\n(2) Navaja Pioja, Daño 6.\n>>>>>"))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 6
        else:
            print("Valor inválido, inténtalo de nuevo")
            self.escoger_Navaja()

# Clase Mago que hereda de Personaje
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, grimorio):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.grimorio = grimorio

    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("- Grimorio:", self.grimorio)

    def dañar(self, enemigo):
        return self.inteligencia * self.grimorio - enemigo.defensa

    def escoger_grimorio(self):
        opcion = int(input("Escoge tu grimorio:\n(1) El grimorio de los 4 tréboles, Daño 10.\n(2) El grimorio de los demonios, Daño 13.\n>>>>>"))
        if opcion == 1:
            self.grimorio = 10
        elif opcion == 2:
            self.grimorio = 13
        else:
            print("Valor inválido, inténtalo de nuevo")
            self.escoger_grimorio()

# Crear objetos
persona = Personaje("Angel Suarez", 20, 15, 10, 100)
arturoSuarez = Guerrero("Arturo Suarez", 20, 15, 10, 100, 5)
Gandalf = Mago("Gandalf", 20, 15, 10, 100, 5)

# Atributos antes de la pelea
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
Gandalf.imprimir_atributos()

# Inicia la pelea
persona.atacar(arturoSuarez)
arturoSuarez.atacar(Gandalf)
Gandalf.atacar(persona)

# Atributos después de la pelea
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
Gandalf.imprimir_atributos()
