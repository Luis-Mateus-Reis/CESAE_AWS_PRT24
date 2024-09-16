#Ler primeiro valor
valor1 = int(input("Introduza o 1º valor: "))
#Ler segundo valor
valor2 = int(input("Introduza o 2º valor: "))
print("A permutar os valores usando uma variável temporária...")
#Guardar numa variável temporária o primeiro valor
temp = valor1
#Colocar a primeira variável como segundo valor
valor1 = valor2
#Atribuir a segunda variável com o valor temporário
valor2 = temp
print(f"O 1º valor agora é: {valor1}")
print(f"O 2º valor agora é: {valor2}")

#########################

print("A permutar os valores usando atribuição simultânea de 2 variáveis...")
valor1, valor2 = valor2, valor1
print(f"O 1º valor agora é: {valor1}")
print(f"O 2º valor agora é: {valor2}")

########################

print("A permutar os valores usando um 3º método...")

valor1 = valor1 + valor2
valor2 = valor1 - valor2
valor1 = valor1 - valor2

print(f"O 1º valor agora é: {valor1}")
print(f"O 2º valor agora é: {valor2}")