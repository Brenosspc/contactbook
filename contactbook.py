#menu
tarefa = []
while True:
    print("Agenda telefonica - Menu de opcoes")
    print("1- Mostrar contatos")
    print("2- Adicionar contato")
    print("3- Listar contato")
    print("4- Editar contato")
    print("5- Marcar/Desmarcar como favorito")
    print("6- Listar favorito")
    print("7- Deletar contato")
    print("8- Encerrar programa")

    escolha = input("Digite a sua escolha: ")

    if escolha == "2":
        nome = input("Digite o nome do novo contato: ")
        telefone = input("Digite o numero do novo contato: ")
        email = input("Digite o email do novo contato: ")

        while True:
            resp = input("Desejar colocar esse contato como favorito? (S/N)").strip().upper()
            if resp == "S":
                favorito = True
                print (f"{nome} foi adicionado aos favoritos")
                break
            elif resp == "N":
                favorito = False
                print(f"{nome} nao foi adicionado aos favoritos")
                break
            else:
                print("Resposta invalida, digite S ou N")
            
    novo_contato = {
                "nome": nome,
                "telefone": telefone,
                "email": email,
                "favorito": favorito
            }
    tarefa.append(novo_contato)
    print(f"Contato {nome} adicionado com sucesso")

    if escolha == "8":
        break
1
print("Programa finalizado!")
