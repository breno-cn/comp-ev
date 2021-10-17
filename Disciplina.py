from typing import List
import numpy as np
from horario import Horario

import sys

def parseHorarios(horarios: str) -> List[Horario]:
    # print(horarios)
    horariosArr = horarios.split(', ')
    return list(map(lambda horario: Horario(horario), horariosArr))

class Disciplina:

    def __init__(self, cod: str, nome: str, curso: str, ch: int, horarios: str) -> None:
        self.cod: str = cod
        self.nome: str = nome
        self.curso: str = curso
        self.ch: int = ch
        self.horarios: List[Horario] = parseHorarios(horarios)
        self.horasAulas: int = len(self.horarios)

        # horariosDivididos = np.split(np.array(horarios.split(', ')), 2)
        # self.horarios = list(map(lambda horario: Horario(horario), horariosDivididos))


    def __repr__(self) -> str:
        return f'(cod={self.cod}, nome={self.nome}, curso={self.curso}, ch={self.ch}, horarios={self.horarios}, horasAulas={self.horasAulas})'
