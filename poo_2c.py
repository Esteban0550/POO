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
