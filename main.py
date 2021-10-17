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

    return disciplinasDf


# Cria uma solução válida aleatória
def criaSolucaoInicial(disciplinas: DataFrame, prioridade: DataFrame):
    for indice in prioridade['Docente']:
        # sorteia uma disciplina aleatória para "servir de base" e retira ela do conjunto de disciplinas disponíveis
        # disciplina = random.choice(disciplinas)
        disciplina = random.sample(disciplinas, 1)[0]
        disciplinas.remove(disciplina)
        
        docente = Docente(indice)
        docente.adicionarDisciplina(disciplina)
        
        # print(f'disciplina: {disciplina}')
        # print('\n\n\n')


def main():
    horariosDf = pd.read_csv('horarios.csv', sep=',')
    prioridadesDf = pd.read_csv('prioridades.csv', sep=',')

    # print(horariosDf.iloc[[17]]) 

    disciplinas = criaDisciplinas(horariosDf)
    print(disciplinas)

    # print(pd.DataFrame(disciplinas))
    sys.exit(0)

    criaSolucaoInicial(disciplinas, prioridadesDf)

main()
