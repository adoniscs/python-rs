import os
import sys

sys.path.append(os.path.abspath("../"))
import utils

while True:
    utils.limpar_terminal()
    print("1. Adicionar um contato")
    print("2. Editar um contato ")
    print("3. Deletar um contato")
    print("4. Favoritar um contato")
    print("5. Sair")

    opcao = int(input("Informe uma opção desejada: "))

    if opcao == 1:
        print("Adicionar contato")

    elif opcao == 2:
        print("Editar um contato ")

    elif opcao == 3:
        print("Deletar um contato")

    elif opcao == 5:
        print("Programa finalizado. Até mais!")
        break
