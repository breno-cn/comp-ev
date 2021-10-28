from typing import List
from Disciplina import Disciplina

HORAS_AULAS_VALIDAS = [8, 10, 12]

class Docente:

    def __init__(self, indice: str) -> None:
        self.indice = indice
        self.disciplinas: List[Disciplina] = []

    def horasAulas(self) -> int:
        return sum(map(lambda disciplina: disciplina.ch, self.disciplinas))

    def adicionarDisciplina(self, disciplina: Disciplina) -> bool:
        # verifica se as horas aulas continuam validas
        novasHorasAulas = self.horasAulas() + disciplina.ch
        if not (novasHorasAulas <= 8 ):
            return False
        
        # verifica se haverá apenas dois periodos
        turnosAtuais = set()
        for disciplina in self.disciplinas:
            for horario in disciplina.horarios:
                turnosAtuais.add(horario.turno)
        novosTurnos = set([h.turno for h in disciplina.horarios])
        turnosAtuais.union(novosTurnos)
        if len(turnosAtuais) > 2:
            return False
        
        #não primeiro e ultimo
        for i in self.disciplinas:
            for horariodoc in i.horarios:
                for horariodisc in disciplina.horarios:
                    if(horariodoc.ultimo and horariodisc.primeiro) or (horariodisc.ultimo and horariodoc.primeiro):
                        return False

        # verifica se a nova disciplina não está já na mesma turma que outra
        turmas = set([d.turma for d in self.disciplinas])
        turmas.add(disciplina.turma)
        if len(turmas) > 2:
            return False



        return True

    def verificaHoras(self) -> bool:
        hora_aula = 0
        for disciplina in self.disciplinas:
            hora_aula += disciplina.ch
        
        if hora_aula == 8 or hora_aula == 10 or hora_aula == 12:
            return True
        

        return False

    def __repr__(self) -> str:
        return f'(indice={self.indice}, disciplinas={self.disciplinas})'
