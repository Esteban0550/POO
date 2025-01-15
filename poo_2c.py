class Personaje:
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
 
    def imprimir_atributos(self):
        print(self.__nombre)
        print("-Fuerza: ", self.__fuerza)
        print("-Inteligencia: ", self.__inteligencia)
        print("-Defensa: ", self.__defensa)
        print("-Vida: ", self.__vida)
   
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa
 
    def esta_vivo(self):
        return self.__vida > 0
   
    def morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")
 
    def dañar(self, enemigo):
        daño = self.__fuerza - enemigo.__defensa
        if daño > 0:
            return daño
        else:
            return 0
 
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.__vida = enemigo.__vida - daño
 
        if 0 >= enemigo.__vida:
            enemigo.morir()
 
class Guerrero (Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

arturoSuarez = Guerrero("Arturo Suarez",12, 3000, 2,100, .5)
arturoSuarez.imprimir_atributos()
print("El valor de espada es: ",arturoSuarez.espada)
mi_personaje = Personaje("EstebanDido", 40, 50, 45, 100)
mi_enemigo = Personaje("Angel", 70, 100, 70, 100)

mi_personaje = 0
mi_personaje.imprimir_atributos()
