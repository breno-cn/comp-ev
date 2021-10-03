from os import sep
import pandas as pd

def main():
    horarios = pd.read_csv('horarios.csv', sep=',')
    prioridades = pd.read_csv('prioridades.csv', sep=',')
    # print(horarios.head())
    # print(prioridades.head())

main()
