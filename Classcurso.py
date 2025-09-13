from Classfacultad import facultad

class curso(facultad):
    def __init__(self, titulo_curso, code, cursos, profesor):
        super().__init__(cursos)
        self.titulo_curso = titulo_curso
        self.code = code
        self.profesor = profesor