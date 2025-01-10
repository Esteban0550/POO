<<<<<<< HEAD
class Personaje:
    # Constructor de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    # Método para imprimir los atributos
    def imprimir_atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"- Fuerza: {self.fuerza}")
        print(f"- Inteligencia: {self.inteligencia}")
        print(f"- Defensa: {self.defensa}")
        print(f"- Vida: {self.vida}")

    # Método para subir de nivel
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    # Método para verificar si está vivo
    def esta_vivo(self):
        return self.vida > 0

    # Método para matar al personaje
    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha muerto.")
        
    # Método para calcular el daño infligido
    def dañar(self, enemigo):
        return max(self.fuerza - enemigo.defensa // 2, 0)  # El daño no puede ser negativo
    
    # Método para atacar a otro personaje
    def atacar(self, enemigo):
        if not self.esta_vivo():
            print(f"{self.nombre} no puede atacar porque está muerto.")
            return
        if not enemigo.esta_vivo():
            print(f"{enemigo.nombre} ya está muerto.")
            return
        
        daño = self.dañar(enemigo)
        enemigo.vida -= daño
        print(f"{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}.")
        print(f"La vida de {enemigo.nombre} ahora es {enemigo.vida}.")
        if enemigo.vida <= 0:
            enemigo.morir()

# Instanciar personajes
mi_personaje = Personaje("Esteban", 100, 50, 70, 100)
mi_enemigo = Personaje("Angel", 100, 70, 40, 100)

# Imprimir atributos iniciales
print("Atributos iniciales del personaje:")
mi_personaje.imprimir_atributos()
print("\nAtributos iniciales del enemigo:")
mi_enemigo.imprimir_atributos()

# Realizar un ataque
print("\nAtaque:")
mi_personaje.atacar(mi_enemigo)

# Imprimir atributos después del ataque
print("\nAtributos después del ataque:")
mi_personaje.imprimir_atributos()
mi_enemigo.imprimir_atributos()
=======
class personaje: 
    #Atributos de la clase 
    nombre = "default"
    fuerza = 0
    inteligencia = 0
    vida = 0
    defensa = 0
    #indicar que no se hara nada por el momento 
    pass
#es una variable del constructor vacio
mi_personaje = personaje()
#modificando valores de los atributos

mi_personaje.nombre = "EstebanDido"
mi_personaje.fuerza = 300
mi_personaje.inteligencia = -2
mi_personaje.vida = 150
mi_personaje.defensa = 100

print ("el nombre de mi personaje es:",mi_personaje.nombre)
print ("la fuerza de mi personaje es:",mi_personaje.fuerza)
print ("la vida de mi personaje es:",mi_personaje.vida)
print ("la inteligencia de mi personaje es:",mi_personaje.inteligencia)
print ("la defesna  de mi personaje es:",mi_personaje.defensa)
>>>>>>> e34036de1b6abfe3d3323507cc82f20c04780cb6
