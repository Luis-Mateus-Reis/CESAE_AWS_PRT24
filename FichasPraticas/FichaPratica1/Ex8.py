#Ler minuto da 1ª música
min1 = int(input("Introduza os minutos da música 1: "))
#Ler segundo da 1ª música
sec1 = int(input("Introduza os segundos da música 1: "))
#Ler minuto da 2ª música
min2 = int(input("Introduza os minutos da música 2: "))
#Ler segundo da 2ª música
sec2 = int(input("Introduza os segundos da música 2: "))
#Ler minuto da 3ª música
min3 = int(input("Introduza os minutos da música 3: "))
#Ler segundo da 3ª música
sec3 = int(input("Introduza os segundos da música 3: "))
#Ler minuto da 4ª música
min4 = int(input("Introduza os minutos da música 4: "))
#Ler segundo da 4ª música
sec4 = int(input("Introduza os segundos da música 4: "))
#Ler minuto da 5ª música
min5 = int(input("Introduza os minutos da música 5: "))
#Ler segundo da 5ª música
sec5 = int(input("Introduza os segundos da música 5: "))
#Cálculo dos segundos
sum_sec = sec1 + sec2 + sec3 + sec4 + sec5
sec = sum_sec % 60
#Cálculo dos minutos
sum_min = min1 + min2 + min3 + min4 + min5 + sum_sec//60
min = sum_min % 60
#Cálculo das horas
hour = sum_min//60
#Output o resultado final em horas, minutos e segundos
print(f"Total do Álbum: {hour}h {min}m {sec}s")