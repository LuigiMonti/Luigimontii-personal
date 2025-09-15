class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
      

    # @property
    # def nombre(self):
    #     return self.__nombre 
    
    # @nombre.setter
    # def nombre(self, nuevo_nombre):
    #     self.__nombre = nuevo_nombre

    # @property
    # def edad(self):
    #     return self.__edad
    
    # @edad.setter
    # def edad(self, nueva_edad):
    #     self.__edad = nueva_edad

personas = []

for i in range(3):
    nombre = input (f'Ingrese su nombre:  ')
    edad = int(input(f'Ingrese la edad de {nombre} '))

    p = Persona(nombre,edad)
    personas.append(p)

print("\nLista de personas registradas:")
for persona in personas:
    print(f"Nombre: {persona.nombre}, Edad: {persona.edad}")    

    
