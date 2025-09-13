from Classcurso import curso

class profesor(curso):
    def __init__(self, nombre_profesor, id_profe):
        super().__init__()
        self.nombre = nombre_profesor
        self.id = id_profe
