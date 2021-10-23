from os import sep
from typing import List, Set
import pandas as pd
from pandas.core.frame import DataFrame
from Disciplina import Disciplina

import numpy as np

import random

import sys
from Docente import Docente

from horario import Horario

def criaDisciplinas(horariosDf: DataFrame) -> Set[Disciplina]:
    disciplinas = []

    for i in range(len(horariosDf)):
        coluna = horariosDf.iloc[[i]].values[0]
        cod = coluna[0]
        nome = coluna[1]
        curso = coluna[2]
        ch = coluna[3]
        horarios = coluna[4]

        # print(coluna)
        # print(horarios)

        disciplina = Disciplina(cod, nome, curso, ch, horarios)
        disciplinas.append(disciplina)
        # disciplinas.add(disciplina)

    disciplinasDf = pd.DataFrame([x.dicionario() for x in disciplinas])
    # print('*')

    return disciplinasDf


def proxDisciplinaDisponivel(docente: Docente, disciplinas: DataFrame) -> Disciplina:
    horasAulas = docente.horasAulas()
    horasAulasCompativeis = disciplinas.query('(horasAulas + @horasAulas < 8) or (horasAulas + @horasAulas == 10) or (horasAulas + @horasAulas == 12)')
    # print(horasAulasCompativeis)
    return horasAulasCompativeis.sample(n=1)


# Cria uma solução válida aleatória
def criaSolucaoInicial(disciplinas: DataFrame, prioridade: DataFrame):
    for indice in prioridade['Docente']:
        # cria um objeto docente para trabalhar
        docente = Docente(indice)

        # sorteia uma disciplina aleatória para "servir de base" e retira ela do conjunto de disciplinas disponíveis
        disciplina = disciplinas.sample(n=1).iloc[[0]].to_dict()

        print(disciplina)
        sys.exit(0)
        # docente.adicionarDisciplina(disciplina)
        
        # verifica quais disciplinas ainda estão disponíveis que obedecem as regras
        disponiveis = proxDisciplinaDisponivel(docente, disciplinas)

        print('=' * 50)
        print(disponiveis)
        print('=' * 50)
        
        # print(f'disciplina: {disciplina}')
        # print('\n\n\n')


def main():
    horariosDf = pd.read_csv('horarios.csv', sep=',')
    prioridadesDf = pd.read_csv('prioridades.csv', sep=',')

    # print(horariosDf.iloc[[17]]) 

    disciplinas = criaDisciplinas(horariosDf)
    print(disciplinas)

    # print(pd.DataFrame(disciplinas))
    # sys.exit(0)

    # criaSolucaoInicial(disciplinas, prioridadesDf)

if __name__ == '__main__':
    main()
