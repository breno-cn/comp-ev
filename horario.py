import numpy as np

diaParaNumero = {
    'Segunda-feira': 0,
    'Terça-feira': 1,
    'Quarta-feira': 2,
    'Quinta-feira': 3,
    'Sexta-feira': 4,
    'Sábado': 5
}

def horarioParaNumero(horario: str) -> int:
    partes = horario.split(' ')

    print(partes)

    dia = partes[0]
    horarioStr = partes[1].split('h:')

    print(horarioStr)

    hora = int(horarioStr[0])
    minuto = int(horarioStr[1])

    return (diaParaNumero[dia] * 24 * 60) + (hora * 60) + minuto


class Horario:

    def __init__(self, partes: str) -> None:
        # print(textoHorario)
        # partes = textoHorario.split(', ')

        print(f'PARTES={partes}')

        self.inicio = horarioParaNumero(partes[0])
        self.fim = horarioParaNumero(partes[1])

    def __str__(self) -> str:
        return f'(inicio={self.inicio}, fim={self.fim})'

    def __repr__(self) -> str:
        return f'(inicio={self.inicio}, fim={self.fim})'
