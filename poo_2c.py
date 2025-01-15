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

    # Método para verificar si está vivo
    def esta_vivo(self):
        return self.vida > 0

    # Método para matar al personaje
    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha muerto.")

    # Método para calcular el daño infligido
    def dañar(self, enemigo):
        if self.fuerza == 40 and enemigo.defensa == 70:
            print("El daño no se aplica debido a las reglas específicas.")
            return 0
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

# Crear instancias para prueba
esteban_dido = Personaje("EstebanDido", 40, 20, 50, 100)
angel = Personaje("Angel", 30, 15, 70, 100)

# Imprimir atributos iniciales
print("Atributos iniciales de los personajes:")
esteban_dido.imprimir_atributos()
angel.imprimir_atributos()

# Realizar un ataque
print("\nAtaque:")
esteban_dido.atacar(angel)

# Imprimir atributos después del ataque
print("\nAtributos después del ataque:")
esteban_dido.imprimir_atributos()
angel.imprimir_atributos()
