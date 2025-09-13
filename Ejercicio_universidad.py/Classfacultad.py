from Classuniversidad import universidad



class facultad(universidad):
    def __init__(self, nombre_facultad, cursos=None):
        super().__init__([])
        
        self.cursos = cursos if cursos is not None else []
        self.nombre_facultad = nombre_facultad

    def ver_facultades(self):
        for i in self.facultad: print('\n',i)
     
    def ver_detalles_facultad(self):
        print(f'{self.nombre_facultad} los cursos de esta facultad son: {self.cursos}')