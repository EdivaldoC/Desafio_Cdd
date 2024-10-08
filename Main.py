nome = [""]*2
senha = [0]*2
tam = len(nome)
escolha = str(input("1 - cadastra \n2 - Visualiza \n3 - Login \n4 - Sair "))
while escolha != 4:
    match escolha:
        case "1":
            for i in range(tam):
                nome [i] = str(input("Digite seu nome: "))
                senha [i] = str(input("Digite a senha: "))
            escolha = str(input("1 - cadastra \n2 - Visualiza \n3 - Login \n4 - Sair "))
        
        case "2":
            for i in range(tam):
                print(nome[i],senha[i],)
                print()
            escolha = str(input("1 - cadastra \n2 - Visualiza \n3 - Login \n4 - Sair "))

        case "3":
            user = input("Digite o nome do usuario: ")
            for i in range(tam):
                if user == nome [i]:
                    sen = input("Digite a senha:")
                    if sen == senha[i]:
                        print("Login efetuado")
                else:
                    print("senha invalida")
            escolha = str(input("1 - cadastra \n2 - Visualiza \n3 - Login \n4 - Sair "))

        case "4":
            print("Fim")
            escolha = 4
