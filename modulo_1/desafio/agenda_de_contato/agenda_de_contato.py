from limpa_terminal.utils import limpar_terminal
limpar_terminal()

def adicionar_contato(contatos, nome, telefone, email):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    contatos.append(contato)
    print("Contato adicionado com sucesso!")
    return

def visualizar_contatos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        favorito = "❤️" if contato["favorito"] else " "
        print(f"{indice}. [{favorito} ], {nome}, {telefone}, {email}")
    return

def editar_contato(contatos, indice, novo_nome, novo_telefone, novo_email):
    indice_ajustado = indice - 1

    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        contatos[indice_ajustado]["nome"] = novo_nome
        contatos[indice_ajustado]["telefone"] = novo_telefone
        contatos[indice_ajustado]["email"] = novo_email
        print(f"Contato {indice} atualizado. {contatos[indice_ajustado]}")
    else:
        print("Indíce inválido. Tente novamente.")
    return

def favoritar_contato(contato, indice):
    indice_ajustado = indice - 1
    contato[indice_ajustado]["favorito"] = True
    print(f"Contato {indice} atualizado para favorito.")
    return

def visualizar_contatos_favoritos(contatos):
    # forma abrevida de percorrer a lista de contatos e armazenas
    # apenas os favoritos - List Comprehension (lista comprimida)
    contatos_favoritos = [contato for contato in contatos if contato["favorito"]]
    
    if not contatos_favoritos:
        print("Nenhum contato favorito na agenda.")
    else:
        print("\nContatos favoritos:")

        for indice, contato in enumerate(contatos_favoritos, start=1):
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]        
            print(f"{indice}. {nome}, {telefone}, {email}")
    return

def deletar_contato(contato, indice):
    indice_ajustado = indice - 1
    contato_removido = contato.pop(indice_ajustado)
    print(f"O contato {contato_removido['nome']} foi deletado com sucesso.")
    return

lista_de_contatos = []

while True:
    print("1. Adicionar um contato")
    print("2. Listar todos os contatos")
    print("3. Editar um contato")
    print("4. Favoritar um contato")
    print("5. Visualizar contato favoritos")
    print("6. Deletar um contato")
    print("7. Sair")

    opcao = int(input("Informe uma opção desejada: "))

    if opcao == 1:
        nome_completo = input("Informe o nome completo: ")
        telefone = int(input("Informe um número de telefone: "))
        email = input("Informe um endereço de email: ")
        adicionar_contato(lista_de_contatos, nome_completo, telefone, email)
        print(f'Contato de "{nome_completo}", com o telefone "{telefone}" e email "{email}" adicionado com sucesso.')

    elif opcao == 2:
        if not len(lista_de_contatos):
            print("\nLista de contato vazia. Adicione um novo contato a lista.")
        else:
            print("\nAgenda de contato:")
            visualizar_contatos(lista_de_contatos)

    elif opcao == 3:
        if not lista_de_contatos:
            print("Agenda Vazia. Adicione um novo contato.")
        else:
            visualizar_contatos(lista_de_contatos)
            indice = int(input("Informe o indice que deseja atualizar: "))
        
            if indice < 1 or indice > len(lista_de_contatos):
                print("Indice inválido. Tente novamente.")
            else:
                nome = input("Informe o nome atualizado: ")
                telefone = int(input("Informe o novo telefone: "))
                email = input("Informe o novo email: ")
                editar_contato(lista_de_contatos, indice, nome, telefone, email)
                print(f"Contato {indice} atualiza com sucesso!")

    elif opcao == 4:
        if not lista_de_contatos:
            print("Agenda Vazia. Adicione um novo contato.")
        else:
            visualizar_contatos(lista_de_contatos)
            indice = int(input("Informe o indice que deseja atualizar: "))
            
            if indice < 1 or indice > len(lista_de_contatos):
                print("Indice inválido. Tente novamente.")
            else:
                favoritar_contato(lista_de_contatos, indice)

    elif opcao == 5:
        if not lista_de_contatos:
            print("Agenda Vazia. Adicione um novo contato.")
        else:
            visualizar_contatos_favoritos(lista_de_contatos)
    
    elif opcao == 6:
        if not lista_de_contatos:
            print("Agenda vazia. Adicione um novo contato.")
        else:
            visualizar_contatos(lista_de_contatos)
            indice = int(input("Informe o indice que deseja apagar da agenda: "))

            if indice < 1 or indice > len(lista_de_contatos):
                print("Índice inválido. Tente novamente.")
            else:
                deletar_contato(lista_de_contatos, indice)

    elif opcao == 7:
        break

print("Programa finalizado. Até mais!")