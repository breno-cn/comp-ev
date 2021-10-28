from typing import List
import numpy as np
from horario import Horario
from horario import diaParaNumero

import sys

def parseHorarios(horarios: str) -> List[Horario]:
    # print(horarios)
    horariosArr = horarios.split(', ')
    return list(map(lambda horario: Horario(horario), horariosArr))

def turmaDeGBC(cod: str) -> int:
    return int(cod[-2])

def turmaDeGSI(cod: str) -> int:
        id = int(cod[-2:])

        if id >= 1 and id <= 5:
            return 10
        
        if id >= 6 and id <= 10:
            return 20
        
        if id >= 11 and id <= 15:
            return 30

        if id >= 16 and id <= 20:
            return 40

        if id >= 21 and id <= 25:
            return 50

        if id >= 26 and id <= 30:
            return 60

        if id >= 31 and id <= 35:
            return 70

        if id >= 46 and id <= 79:
            return 80

# BSI = *10
# eng quimica = *100
# fisica medica = *1000
# matematica = * 10000
# GSI = * 100000
        
def turmaDeFACOM(cod: str) -> int:
    turmas = {
        'FACOM31701': 9 * 10,
        'FACOM39017': 1 * 100,
        'FACOM39018': 4 * 1000,
        'FACOM39020': 2 * 10000,
        'FACOM39101': 1 * 100000,
        'FACOM39201': 2 * 100000,
        'FACOM39302': 3 * 100000,
        'FACOM39401': 4 * 100000,
        'FACOM39501': 5 * 100000,
        'FACOM39502': 5 * 100000,
        'FACOM39601': 6 * 100000,
        'FACOM39602': 6 * 100000,
        'FACOM39702': 7 * 100000,
        'FACOM39801': 8 * 100000,
        'FACOM39802': 8 * 100000,
        'FACOM39803': 8 * 100000,
        'FACOM39301': 3 * 100000,
        'FACOM49010(U)': 1 * 1000000,
        'FACOM49010(V)': 1 * 1000000,
        'FACOM49050': 5 * 1000000,
        'FACOM49060': 6 * 1000000,
        'FACOM49070': 7 * 1000000,
        'FACOM49080': 8 * 1000000,
        'FACOM49010(W)': 1 * 1000000
    }

    return turmas[cod]

def turmaDaDisciplina(cod: str) -> int:
    # ONLY SANE OPTION
    if cod.startswith('GBC'):
        return turmaDeGBC(cod)

    if cod.startswith('GSI'):
        return turmaDeGSI(cod)

    if cod.startswith('FACOM'):
        return turmaDeFACOM(cod)

    # casos especiais
    else:
        turmas = {
            'GAG009': 1 * 100000,
            'GBT017': 4 * 1000000,
            'GCI007': 1 * 10000000,
            'GES005': 2 * 100000000,
            'GES009': 3 * 100000000,
            'GES013': 4 * 100000000,
            'GFM015': 2 * 1000000000,
            'GGI036': 7 * 10000000000,
            'GGI041': 7 * 10000000000,
            'PGC101': 9 * 100000000000
        }
        return turmas[cod]


class Disciplina:

    def __init__(self, cod: str, nome: str, curso: str, ch: int, horarios: str) -> None:
        self.cod: str = cod
        self.nome: str = nome
        self.curso: str = curso
        self.ch: int = ch
        self.horarios: List[Horario] = parseHorarios(horarios)
        self.horasAulas: int = len(self.horarios)
        self.turma = turmaDaDisciplina(self.cod)

        # horariosDivididos = np.split(np.array(horarios.split(', ')), 2)
        # self.horarios = list(map(lambda horario: Horario(horario), horariosDivididos))

    def turnos(self) -> List[str]:
        return [h.turno for h in self.horarios]
    
    # Esse método é utilizado para converter uma lista de disciplinas em um DataFrame
    def dicionario(self):
        return {
            'cod': self.cod,
            'nome': self.nome,
            'curso': self.curso,
            'ch': self.ch,
            'horarios': self.horariosParaCsv(),
            'horasAulas': self.horasAulas
        }

    def horariosParaCsv(self) -> str:
        return ';'.join(map(lambda x: x.csv(), self.horarios))

    def __repr__(self) -> str:
        return f'(cod={self.cod}, nome={self.nome}, curso={self.curso}, ch={self.ch}, horarios={self.horarios}, horasAulas={self.horasAulas}), turma={self.turma})'
