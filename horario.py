import numpy as np

diaParaNumero = {
    'Segunda-feira': 0,
    'Terça-feira': 1,
    'Quarta-feira': 2,
    'Quinta-feira': 3,
    'Sexta-feira': 4,
    'Sábado': 5
}

HORA_AULA = 50

def parseHora(inicio: str) -> int:
    return int(inicio.split(' ')[1].split('h:')[0])

def horarioParaNumero(horario: str) -> int:
    partes = horario.split(' ')

    # print(partes)

    dia = partes[0]
    horarioStr = partes[1].split('h:')

    # print(horarioStr)

    hora = int(horarioStr[0])
    minuto = int(horarioStr[1])

    return (diaParaNumero[dia] * 24 * 60) + (hora * 60) + minuto

def parseTurno(inicio: str) -> str:
    # Terça-feira 21h:40
    hora = parseHora(inicio)
    
    if hora >= 7 and hora <= 12:
        return 'MANHA'
    if hora >= 12 and hora <= 18:
        return 'TARDE'
    if hora >= 18:
        return'NOITE'

def parseDia(inicio:str) -> str:
    # Terça-feira 21h:40
    dia = inicio.split(' ')[0]
    return dia

def ehPrimeiro(inicio: int) -> bool:
    hora = parseHora(inicio)
    return hora == 7

def ehUltimo(inicio: int) -> bool:
    hora = parseHora(inicio)
    return hora == 20



class Horario:

    def __init__(self, inicio: str) -> None:
        # print(textoHorario)
        # partes = textoHorario.split(', ')

        # print(f'PARTES={partes}')

        self.inicio = horarioParaNumero(inicio)
        self.fim = self.inicio + HORA_AULA
        self.turno = parseTurno(inicio)
        self.dia = parseDia(inicio)
        self.primeiro = ehPrimeiro(inicio)
        self.ultimo = ehUltimo(inicio)

    def diaParaNumero(self):
        return diaParaNumero[self.diaParaNumero]

    # Método utilizado para usar o objeto em um DatFrame
    def csv(self) -> str:
        return f'{self.inicio}-{self.fim}'

    def __str__(self) -> str:
        return f'(inicio={self.inicio}, fim={self.fim}, turno={self.turno}, dia={self.dia}, primeiro={self.primeiro}, ultimo={self.ultimo})'

    def __repr__(self) -> str:
        return f'(inicio={self.inicio}, fim={self.fim}, turno={self.turno}, dia={self.dia}, primeiro={self.primeiro}, ultimo={self.ultimo})'


# 
# segunda 07:10 =  1
# segunda 8:00 = 2
# segunda 20:00 = 10
# terça 7:10 = 11
# 