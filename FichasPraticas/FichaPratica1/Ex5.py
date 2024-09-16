#Ler o primeiro valor
val1 = float(input("Introduz o 1º valor: "))
#Ler o segundo valor
val2 = float(input("Introduz o 2º valor: "))
#Ler o terceiro valor
val3 = float(input("Introduz o 3º valor: "))
#Cálculo e output da média aritmética
print(f"A média aritmética é: {(val1+val2+val3)/3:.1f}")
#Cálculo e output da média ponderada
print(f"A média ponderada (20%, 30% e 50%) é: {val1*0.2+val2*0.3+val3*0.5:.1f}")
#Cálculo e output da média geométrica
print(f"A média geométrica é: {(val1*val2*val3)**(1/3):.1f}")