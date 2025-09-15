class Universidad:
    def __init__(self, nombre_universidad, facultades):
        self.nombre_universidad = nombre_universidad
        self.facultades = facultades if facultades is not None else []
        # self.lista_facultades = []


    def crear_facultad(self, nueva_facultad):
        self.facultades.append(nueva_facultad)
        print(f'La nueva facultad de la universidad es {nueva_facultad}\n')
        print('FACULTADES:')

        for i in self.facultades:
            print(i)

nueva_facultad = input('Qué facultad se agregagará a la universidad? ')  

UFM = Universidad('UFM', ['Ciencias economicas', 'Arquitectura', 'Medicina'])
UFM.crear_facultad(nueva_facultad)







