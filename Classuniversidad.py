class universidad:
    def __init__(self,facultad):
        self.facultad = facultad if facultad is not None else []
        
    def agregar_facultades(self,faculty):
        self.facultad.append(faculty)
        print(f'Se ha agregado {faculty} correctamente!!')
        print(self.facultad)
    

    def agregar_profesor(self,professor):
        pass




        




