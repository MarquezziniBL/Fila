L = []

while True:
    print(f"fila atual {L}")
    print("Escolha uma das opções abaixo:")
    opcao = int(input("1- Por alguém na fila, 2- Chamar o Próximo: "))
    try:
        if opcao == 1:
            try:
                x = 0
                for i in L:
                    x += 1
                L.append(L[x-1]+1)
                print(L)
            except IndexError:
                L.append(1)
                print(L)
        elif opcao == 2:
            L.remove(L[0])
            print(L)
        else:
            print("Opcão indisponível")
    except IndexError:
        print("Fila vazia")
        add = str(input("deseja adicionar um item (s\n): "))
        if add == 's':
            L.append(1)
        else:
            break
