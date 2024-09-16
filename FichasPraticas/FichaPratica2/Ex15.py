num1 = float(input("Indica o 1º número: "))
num2 = float(input("Indica o 2º número: "))
num3 = float(input("Indica o 3º número: "))

ordem = input("Ordem Crescente (C) ou Ordem Decrescente (D)?")

if ordem == "C":
    if num1 <= num2 <= num3:
        print(f"{num1}, {num2}, {num3}")
    elif num1 <= num3 <= num2:
        print(f"{num1}, {num3}, {num2}")
    elif num2 <= num3 <= num1:
        print(f"{num2}, {num3}, {num1}")
    elif num2 <= num1 <= num3:
        print(f"{num2}, {num1}, {num3}")
    elif num3 <= num1 <= num2:
        print(f"{num3}, {num1}, {num2}")
    elif num3 <= num2 <= num1:
        print(f"{num3}, {num2}, {num1}")
elif ordem == "D":
    if num1 <= num2 <= num3:
        print(f"{num3}, {num2}, {num1}")
    elif num1 <= num3 <= num2:
        print(f"{num2}, {num3}, {num1}")
    elif num2 <= num3 <= num1:
        print(f"{num1}, {num3}, {num2}")
    elif num2 <= num1 <= num3:
        print(f"{num3}, {num1}, {num2}")
    elif num3 <= num1 <= num2:
        print(f"{num2}, {num1}, {num3}")
    elif num3 <= num2 <= num1:
        print(f"{num1}, {num2}, {num3}")
else:
    print("Opção errada, escolhe C ou D!")