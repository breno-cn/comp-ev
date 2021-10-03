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

# Transforma um horário no format XXh:XX para um número
# IMPLEMENTAÇÃO ANTIGA
# def horarioParaNumero(horario: str) -> int:
#     print(f'HORARIO = {horario}')

#     partes = horario.split(':')
#     horas = int(partes[0].replace('h', '')) * 60
#     minutos = int(partes[1])

#     return horas + minutos

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

##############################################
# IMPLEMENTAÇÃO ANTIGA
# class Horario:

#     # faz o parse de uma linha e cria um objeto horário
#     # Exemplo de horário
#     # Segunda-feira 09h:50, Segunda-feira 10h:40, Quinta-feira 08h:50, Quinta-feira 09h:50
#     def __init__(self, line) -> None:
#         partes = np.array(line.split(','))
#         dias = np.split(partes, 2)
#         print(dias)
#         print(dias[0][0].strip())
#         print(dias[0][1].strip())

#         inicio = dias[0][0].strip().split(' ')
#         fim = dias[0][1].strip().split(' ')

#         diaInicio = diaParaNumero[inicio[0]]
#         diaFim = diaParaNumero[fim[0]]

#         self.inicio = diaInicio + horarioParaNumero(inicio[1])
#         self.fim = diaFim + horarioParaNumero(fim[1])

#         print(self.inicio)
#         print(self.fim)
