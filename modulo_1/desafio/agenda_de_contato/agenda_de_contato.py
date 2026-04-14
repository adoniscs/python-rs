def adicionar_contato(contatos, nome, telefone, email):
    # contato: Barbearia
    # nome: Luiz Felipe
    # telefone: 11944332222
    # email: luizf@email.com
    contato = {
        "nome_completo": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    contatos.append(contato)
    print("Contato adicionado com sucesso!")
    return

lista_de_contatos = []

while True:
    print("1. Adicionar um contato")
    print("2. Listar todos os contatos")
    print("3. Editar um contato")
    print("4. Deletar um contato")
    print("5. Favoritar um contato")
    print("6. Sair")

    opcao = int(input("Informe uma opção desejada: "))

    if opcao == 1:
        nome_completo = input("Informe o nome completo: ")
        telefone = int(input("Informe um número de telefone: "))
        email = input("Informe um endereço de email: ")
        adicionar_contato(lista_de_contatos, nome_completo, telefone, email)
        print(f'Contato de "{nome_completo}", com o telefone "{telefone}" e email "{email}" adicionado com sucesso.')

    elif opcao == 2:
        print("Editar um contato ")

    elif opcao == 3:
        print("Deletar um contato")

    elif opcao == 5:
        print("Programa finalizado. Até mais!")
        break
