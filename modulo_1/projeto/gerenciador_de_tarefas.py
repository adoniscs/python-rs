import os
import sys

sys.path.append(os.path.abspath("../../"))
import utils
utils.limpar_terminal()


while True:
    print("\nMenu do gerenciador de Lista de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefa completas")
    print("6. Sair")

    escolha = int(input("Digite a sua escolha: "))

    if escolha == 6:
        break

    utils.limpar_terminal()

print("Programa finalizado")