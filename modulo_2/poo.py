from limpa_terminal.utils import limpar_terminal

limpar_terminal()


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."


pessoa1 = Pessoa("Alice", 30)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa("Arthur", 45)
mensagem2 = pessoa2.saudacao()
print(mensagem2)
