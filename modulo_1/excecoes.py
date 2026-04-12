print("Exemplo de captura de exceção")

try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
except ValueError as e:
    print(f"value error {e}")
    raise ValueError("Tipo de variável incompatível")
except Exception as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Operação finalizada!")
