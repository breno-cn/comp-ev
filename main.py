from os import sep
import pandas as pd
from Disciplina import Disciplina

from horario import Horario

def criaDisciplinas(horariosDf):
    valores = horariosDf.values
    valor = valores[2]

    # print(valores[0:5])
    print(valor)

    disciplina = Disciplina(valor[0], valor[1], valor[2], valor[3], valor[4])

    print('=' * 100)
    print(disciplina.horarios)
    print('=' * 100)
    print(disciplina)

    pass

def main():
    horarios = pd.read_csv('horarios.csv', sep=',')

    # print(horarios.head())


    criaDisciplinas(horarios)

    # print(horarios.values)

    # prioridades = pd.read_csv('prioridades.csv', sep=',')
    # linha = horarios.iloc[[2]]
    # print(linha['Cod. Disciplina'])
    # print(linha['Nome Disciplina'])

    # horario = Horario(horarios['Horarios'][1])

main()
