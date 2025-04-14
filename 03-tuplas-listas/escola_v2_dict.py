#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades
"""

__version__ = "0.1.0"

#Dados
sala1 = ["Erick", "Maia", "Gustavo", "Breno", "Bruno", "Carol" ]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erick", "Maia","Carol", "Carlos", "Antonio"]
aula_musica = ["Erick", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Carol", "Bruno", "Antonio"]

atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica), 
    ("Dança", aula_danca),
]
#Listar aluinos em cada atividade por sala

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno  in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:    
            atividade_sala2.append(aluno)

    print("Sala1", atividade_sala1)
    print("Sala2", atividade_sala2)

    print()
    print("-" * 40)
