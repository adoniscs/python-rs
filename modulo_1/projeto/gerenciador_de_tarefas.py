import os
import sys

sys.path.append(os.path.abspath("../../"))
import utils
utils.limpar_terminal()

def adicionar_tareda(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa: \"{nome_tarefa}\", foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("\nLista de tarefas a fazer: ")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✔️" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
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
        utils.limpar_terminal()
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tareda(tarefas, nome_tarefa)

    elif escolha == 2:
        utils.limpar_terminal()
        ver_tarefas(tarefas)

    elif escolha == 6:
        break


print("Programa finalizado")