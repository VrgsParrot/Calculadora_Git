import math

print("=== CALCULADORA AVANÇADA ===")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência")
print("6 - Porcentagem")
print("7 - Raiz quadrada do primeiro número")

opcao = input("Digite a opção desejada: ")

if opcao == "1":
    print("Resultado:", num1 + num2)

elif opcao == "2":
    print("Resultado:", num1 - num2)

elif opcao == "3":
    print("Resultado:", num1 * num2)

elif opcao == "4":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Erro: não é possível dividir por zero.")

elif opcao == "5":
    print("Resultado:", num1 ** num2)

elif opcao == "6":
    print("Resultado:", (num1 * num2) / 100)

elif opcao == "7":
    if num1 >= 0:
        print("Resultado:", math.sqrt(num1))
    else:
        print("Erro: não é possível calcular raiz quadrada de número negativo.")

else:
    print("Opção inválida.")