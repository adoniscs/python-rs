from limpa_terminal.utils import limpar_terminal
limpar_terminal()

from calculadora import divisao, multiplicacao, soma, subtracao

num1 = 100
num2 = 9

resultado_soma = soma(num1, num2)
resultado_subtracao = subtracao(num1, num2)
resultado_multiplicacao = multiplicacao(num1, num2)
resultado_divisao = divisao(num1, num2)

print(f"resultado de {num1} + {num2} = {resultado_soma}")
print(f"resultado de {num1} - {num2} =  {resultado_subtracao}")
print(f"resultado de {num1} x {num2} =  {resultado_multiplicacao}")
print(f"resultado de {num1} ÷ {num2} =  {resultado_divisao:.2f}")
