from Classfacultad import facultad

class curso(facultad):
    def __init__(self, titulo_curso, code, cursos, profesor, nombre_facultad):
        super().__init__(cursos, nombre_facultad)
        self.titulo_curso = titulo_curso
        self.code = code
        self.profesor = profesor

        