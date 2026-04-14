def adicionar_contato(lista_de_contatos, nome, telefone, email):
    # contato: Barbearia
    # nome: Luiz Felipe
    # telefone: 11944332222
    # email: luizf@email.com
    contato = {
        "contato": lista_contatos,
        "nome_completo": nome,
        "telefone": telefone,
        "email": email,
    }
    lista_de_contatos.append(contato)
    print("Contato adicionado com sucesso!")
    return


def listar_contatos(lista_de_contatos):
    print("\nLista de todos os contatos")
    for indice, contato in enumerate(lista_de_contatos, start=1):
        contato_favorito = "❤️" if lista_de_contatos["favorito"] else " "
        nome_contato = contato["nome"]
        numero = contato["numero"]
        email = contato["email"]
        print(f"{indice}. [{contato_favorito}] {nome_contato}, {numero}, {email} ")
    return


lista_de_contatos = []

while True:
    print("1. Adicionar um contato")
    print("2. Editar um contato ")
    print("3. Deletar um contato")
    print("4. Favoritar um contato")
    print("5. Sair")

    opcao = int(input("Informe uma opção desejada: "))

    if opcao == 1:
        nome_completo = input("Informe o come completo: ")
        telefone = int(input("Informe um número de telefone: "))
        email = input("Informe um endereço de email: ")
        adicionar_contato(lista_de_contatos, nome_completo, telefone, email)
        print("Adicionar contato")

    elif opcao == 2:
        listar_contatos(lista_de_contatos)
        print("Editar um contato ")

    elif opcao == 3:
        print("Deletar um contato")

    elif opcao == 5:
        print("Programa finalizado. Até mais!")
        break
