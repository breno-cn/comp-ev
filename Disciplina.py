import numpy as np
from horario import Horario

class Disciplina:

    def __init__(self, cod: str, nome: str, curso: str, ch: int, horarios: str) -> None:
        self.cod = cod
        self.nome = nome
        self.curso = curso
        self.ch = ch

        horariosDivididos = np.split(np.array(horarios.split(', ')), 2)
        self.horarios = list(map(lambda horario: Horario(horario), horariosDivididos))


    def __repr__(self) -> str:
        return f'(cod={self.cod}, nome={self.nome}, curso={self.curso}, ch={self.ch}, horarios={self.ch})'
