num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num3:
    print("O maior número é: ", num1)
elif num2 > num1 and num3:
    print("O maior número é: ", num2)
elif num3 > num1 and num2:
    print("O maior número é: ", num3)