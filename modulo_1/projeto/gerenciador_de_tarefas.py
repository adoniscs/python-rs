import os
import sys

sys.path.append(os.path.abspath("../../"))
import utils
utils.limpar_terminal()

def adicionar_tareda(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

tarefas = []

while True:
    print("\nMenu do gerenciador de Lista de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefa completas")
    print("6. Sair")

    escolha = int(input("Digite a sua escolha: "))

    if escolha == 1:

        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tareda(tarefas, nome_tarefa)

    elif escolha == 6:
        break


print("Programa finalizado")