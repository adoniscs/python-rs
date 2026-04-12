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
        status = "✔️ " if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    """tratado esse indice pois no enumerate informo que indice inicia em 1
    e a lista por padrão inicia em 0. Então preciso subtrair 1 para que
    o número da lista de tarefa informado seja igual ao número do indice da lista que será atualizado"""
    indice_tarefa_ajustado = indice_tarefa - 1

    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa: \"{indice_tarefa}\" atualizada para \"{novo_nome_tarefa}\".")
    else:
        print("Número de tarefa inválido. Tente novamente!")
    return

def completar_tarefa(tarefas, indice_tarefa):
    utils.limpar_terminal()
    indice_tarefa_ajustado = indice_tarefa - 1 # criar uma função para esta linha pois se repete
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print(f"Tarefa {indice_tarefa} concluída com sucesso.")

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
    
    elif escolha == 3:
        utils.limpar_terminal()
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o número da tarefa que deseja atualizar: "))
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)

    elif escolha == 4:
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o número da tarefa que deseja completar: "))
        completar_tarefa(tarefas, indice_tarefa)

    elif escolha == 6:
        break


print("Programa finalizado")