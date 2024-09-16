print("Menu\n1. Criar\n2. Atualizar \n3. Eliminar \n4. Sair")

menu = int(input())

match menu:
    case 1:
        print("Criar")
    case 2:
        print("Atualizar")
    case 3:
        print("Eliminar")
    case 4:
        print("")
    case _:
        print("Opção inválida!")