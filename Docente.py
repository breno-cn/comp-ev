from typing import List
from Disciplina import Disciplina

HORAS_AULAS_VALIDAS = [8, 10, 12]

class Docente:

    def __init__(self, indice: str) -> None:
        self.indice = indice
        self.disciplinas: List[Disciplina] = []

    def horasAulas(self) -> int:
        return sum(map(lambda disciplina: disciplina.horasAulas, self.disciplinas))

    def adicionarDisciplina(self, disciplina: Disciplina) -> None:
        novasHorasAulas = self.horasAulas() + disciplina.horasAulas
        if novasHorasAulas in HORAS_AULAS_VALIDAS:
            self.disciplinas.append(disciplina)
            print(f'disciplina {disciplina.cod} pode ser adicionada')
            return

        print(f'disciplina {disciplina.cod} nao pode ser adicionada')
