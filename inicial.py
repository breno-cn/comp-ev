from typing import Set
import random

from pandas import DataFrame
from Disciplina import Disciplina

from Docente import Docente

def proxDisciplinasPorCH(disciplinas: Set[Disciplina], docente: Docente, df: DataFrame) -> Set[Disciplina]:

    pass

def solucaoInicial(disciplinas: Set[Disciplina], prioridades: DataFrame, df: DataFrame):
    for disciplina in disciplinas:
        print(disciplina)

    # percorre todos os professores pelo indice da planilha prioridades.csv
    for indice in prioridades['Docente']:
        # cria um objeto Docente para trabalhar
        docente = Docente(indice)

        # para cada Docente, sortear disciplinas que atendem a todas as regras consideradas
        # sorteia uma disciplina inicial para servir de base e retira ela do total 
        # e adiciona ela ao docente
        inicialIndice = df.sample(n=1)
        inicial = inicialIndice.to_numpy[0]
        cod = inicial[0]
        nome = inicial[1]
        curso = inicial[2]
        ch = inicial[3]
        horarios = inicial[4]
        disciplina = Disciplina(cod, nome, curso, ch, horarios)        
        disciplinas.remove(inicial)
        docente.adicionarDisciplina(inicial)

        # entra em um loop, e continua adicionando disciplinas que obedecem as regras
        # enquanto não completar 8, 10 ou 12 horas aulas
        while True:
            # proxDisciplina = 
            break
