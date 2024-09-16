horas = int(input("Introduza horas: "))
minutos = int(input("Introduza minutos: "))

if 1 <= horas <= 11:
    print(f"{horas:02}:{minutos:02} AM")
elif horas == 12:
    print(f"12:{minutos:02} PM")
elif 13 <= horas <= 23:
    print(f"{horas-12:02}:{minutos:02} PM")
else:
    print(f"12:{minutos:02} AM")