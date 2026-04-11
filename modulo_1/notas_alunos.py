import sys
import os

sys.path.append(os.path.abspath("../"))
import utils

utils.limpar_terminal()

# ------------ #
notas_aluno = []

for nota in range(0, 3):
    nota_aluno = float(input("Digite sua nota: "))
    notas_aluno.append(nota_aluno)


    notas = sum(notas_aluno)
    media = notas / len(notas_aluno)

if media > 7:
    print(f"Aluno aprovado com média {media:.2f}")
elif media > 6:
    print(f"Aluno de recuperção com média {media:.2f}")
else:
    print(f"Aluno reprovado com média {media:.2f}")
    