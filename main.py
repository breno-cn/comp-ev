import itertools
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
import horario

from itertools import compress, product

from inicial import solucaoInicial


def horasAulasInvalidas(docentes: List[Docente]) -> List[Docente]:
    return [d for d in docentes if d.horasAulas() < 8]

    # for docente in docentes:
        # print(f'docente: {docente.indice}, CH: {docente.horasAulas()}')

#loop de professores dentro de loop de disciplinas
#a disciplina pega as materias que o professor ja tem e aplica as regras 
# se for valida adiciona 
def primeiraSolucao(disciplinas: List[Disciplina], docentes: List[Docente], prioridades: DataFrame) -> List[List[any]]:
    docscompletos = []
    discobtidas = []
    disciplinasCopia = list(disciplinas)
    for disciplina in disciplinas:
        for docente in docentes:
            # if materia in docente.possiveismaterias
            #   faz issae
            # else
            #   passa

            if disciplina.cod in prioridades[prioridades.Docente == docente.indice].values[0][1:]:
                if docente.adicionarDisciplina(disciplina) and disciplina in disciplinasCopia:
                    if disciplina not in docente.disciplinas: 
                        docente.disciplinas.append(disciplina)
                    if docente.verificaHoras():
                        docscompletos.append(docente)
                    discobtidas.append(disciplina)
                    disciplinasCopia.remove(disciplina) 
                    # print('-' * 100)
                    # print(docente)
                    # print('-' * 100)
                    break
          
    for d in discobtidas:
        disciplinas.remove(d)
    
    for doc in docentes:
        docentes.remove(doc)

    #[1,2,3,4,5] - [1,4] = [2, 3, 5]
    
    for docente in docentes:
        print('-' * 100)
        print(docente)
        print('-' * 100)

    return disciplinas, docentes




# O(2^n) kkkkkkkkkkkkkkkkkkkkkkk
def combinacoes(items: List[any]) -> List[List[any]]:
    return ( list(compress(items,mask)) for mask in product(*[[0,1]]*len(items)) )



# OK
def horariosPermitidos(disciplinas: List[Disciplina]) -> List[List[Disciplina]]:
    # possiveisHorarios = [[d1, d2, d3] for d1 in disciplinas for d2 in disciplinas for d3 in disciplinas if d1.horasAulas + d2.horasAulas + d3.horasAulas in [8, 10, 12]]
    # combinacoesDisciplinas = combinacoes(disciplinas)

    # return [lista for lista in combinacoesDisciplinas if sum([d.horasAulas for d in lista]) in [8, 10, 12]]

    # discMap[1] = [d]
    # disciplinas[4] = [dsa]

    # cria um map de horas aulas para usar de referencias na disciplinas
    mapHorasAulas = {
        1: [],
        2: [],
        4: [],
        5: [],
        6: [],
        8: []
    }
    for disciplina in disciplinas:
        mapHorasAulas[disciplina.horasAulas].append(disciplina)

    # print(mapHorasAulas)

    # disciplinasCopias = list(disciplinas)
    # for disciplina in disciplinas:
        
    

    # print(possiveisHorarios)
    # return possiveisHorarios

def apenasDoisTurnos(disciplinas: List[Disciplina]) -> bool:
    # return len(set([d for d in disciplinas])) <= 2
    # [filename for path in dirs for filename in os.listdir(path)]
    turnos = [d.turnos for d in disciplinas]
    t = []
    for i in turnos:
        t.append(i)
    
    return len(set(t)) <= 2

# OK
def apenasDoisPeriodos(disciplinas: List[List[Disciplina]]) -> List[List[Disciplina]]:
    return [d for d in disciplinas if apenasDoisTurnos(d)]


# def naoPrimeiro_Ultimo(disciplinas: List[List[Disciplina]]) -> List[List[Disciplina]]:
#     for listaDisciplina in disciplinas:
#         for i in len(range(listaDisciplina)) - 1:
#             if listaDisciplina[i] e ultimo and listaDisciplina[i + 1] e primeiro:
#                 descarta

# OK
def naoPrimeiro_Ultimo(disciplinas: List[List[Disciplina]]) -> List[List[Disciplina]]:
    resultado = []
    for listaDisciplina in disciplinas:
        for i in range(len(listaDisciplina) - 1):
            if not (listaDisciplina[i].horarios[-1].ultimo and listaDisciplina[i + 1].horarios[0].primeiro):
                resultado.append(listaDisciplina)
            # if disciplina.horarios[i].ultimo and disciplina.horarios[i + 1].primeiro and disciplina.horarios[i].diaNumero() - disciplina.horarios[i + 1].diaNumero() == -1:
                    
    return resultado

def apenasUmDocentePorTurma(disciplinas: List[List[Disciplina]]) -> List[List[Disciplina]]:
    resultado = []

    for listaDisciplina in disciplinas:
        # turmas = [d for d in listaDisciplina if d.turma not in [d2.turma for d2 in listaDisciplina]]
        turmas = [d.turma for d in listaDisciplina]
        # print(f'turma: {turmas} {listaDisciplina[2].cod}')
        # if len(set(turmas)) == len(turmas):
        resultado.append(listaDisciplina)

    return resultado


def criaDisciplinas(horariosDf: DataFrame) -> List[Disciplina]:
    disciplinas = []
    # disciplinas = set()

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

    # disciplinas = [d.ch for d in disciplinas]
    # result = [seq for i in range(len(disciplinas), 0, -1) for seq in itertools.combinations(disciplinas, i) if sum(seq) == 8]
    # print(result)

    return disciplinas

    disciplinasDf = pd.DataFrame([x.dicionario() for x in disciplinas])
    # print('*')

    horarios = horariosPermitidos(disciplinas)
    # for horario in horarios:
    #     print(horario)

    turnos = apenasDoisPeriodos(horarios)
    # for turnos in turnos:
        # print(turnos)
        
    validoPrimeiroUltimo = naoPrimeiro_Ultimo(turnos)
    # for valido in validoPrimeiroUltimo:
    #     print(valido)

    naoRepeteTurma = apenasUmDocentePorTurma(validoPrimeiroUltimo)
    for valido in naoRepeteTurma:
        print(valido)
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

        # print(disciplina)
        # sys.exit(0)
        # docente.adicionarDisciplina(disciplina)
        
        # verifica quais disciplinas ainda estão disponíveis que obedecem as regras
        # disponiveis = proxDisciplinaDisponivel(docente, disciplinas)

        # print('=' * 50)
        # print(disponiveis)
        # print('=' * 50)
        
        # print(f'disciplina: {disciplina}')
        # print('\n\n\n')


def main():
    horariosDf = pd.read_csv('horarios.csv', sep=',')
    prioridadesDf = pd.read_csv('prioridades.csv', sep=',')

    # print(horariosDf.iloc[[17]]) 



    disciplinas = criaDisciplinas(horariosDf)
    docentes = [Docente(d) for d in prioridadesDf['Docente'].values]
    
    docentesaux = list(docentes)
    # print(docentes)
    # sys.exit(0)
    disciplinas, docentesaux = primeiraSolucao(disciplinas, docentesaux, prioridadesDf)
    # print(disciplinas)
    for d in disciplinas:
        print(d)
    print('*' * 100)
    for d in docentes:
        print(d)


    print('/' * 100)
    insuficientes = horasAulasInvalidas(docentes)
    for i in insuficientes:
        print(f'{i.indice} {i.horasAulas()}')


    print('+' * 100)
    for i in docentes:
        print(f'{i.indice} {i.horasAulas()}')

    print('-' * 100)
    for i in docentes:
        print(f'{i.indice} {[d.ch for d in i.disciplinas]}')

    # print(docentes)

    
    # inicial = solucaoInicial(disciplinas, prioridadesDf, horariosDf)

    # disciplinas = criaDisciplinas(horariosDf)
    # print(disciplinas)

    # print(pd.DataFrame(disciplinas))
    # sys.exit(0)

    # criaSolucaoInicial(disciplinas, prioridadesDf)

if __name__ == '__main__':
    main()
