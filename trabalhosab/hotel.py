hospedes = []
reservas = []


def cadastrar_hospede():
    print("\n===== CADASTRO DE HOSPEDE =====")

    nome = input("Nome do hospede: ")
    telefone = input("Telefone: ")

    codigo = len(hospedes) + 1

    hospede = {
        "codigo": codigo,
        "nome": nome,
        "telefone": telefone
    }

    hospedes.append(hospede)

    print("Hospede cadastrado com sucesso!")
    print("Codigo do hospede:", codigo)


def listar_hospedes():
    print("\n===== LISTA DE HOSPEDES =====")

    if len(hospedes) == 0:
        print("Nenhum hospede cadastrado.")
    else:
        for hospede in hospedes:
            print("----------------------------")
            print("Codigo:", hospede["codigo"])
            print("Nome:", hospede["nome"])
            print("Telefone:", hospede["telefone"])


def pesquisar_hospede():
    print("\n===== PESQUISAR HOSPEDE =====")

    nome_pesquisa = input("Digite o nome do hospede: ")
    encontrado = False

    for hospede in hospedes:
        if nome_pesquisa.lower() in hospede["nome"].lower():
            print("Hospede encontrado!")
            print("Codigo:", hospede["codigo"])
            print("Nome:", hospede["nome"])
            print("Telefone:", hospede["telefone"])
            encontrado = True

    if encontrado == False:
        print("Hospede nao encontrado.")


def registrar_reserva():
    print("\n===== REGISTRAR RESERVA =====")

    if len(hospedes) == 0:
        print("Cadastre um hospede antes de registrar uma reserva.")
        return

    try:
        codigo = int(input("Codigo do hospede: "))
    except ValueError:
        print("Digite um codigo valido.")
        return

    hospede_encontrado = None

    for hospede in hospedes:
        if hospede["codigo"] == codigo:
            hospede_encontrado = hospede

    if hospede_encontrado is None:
        print("Hospede nao encontrado.")
        return

    quarto = input("Numero do quarto: ")

    quarto_ocupado = False

    for reserva in reservas:
        if reserva["quarto"] == quarto:
            quarto_ocupado = True

    if quarto_ocupado:
        print("Este quarto ja possui uma reserva.")
        return

    try:
        noites = int(input("Quantidade de noites: "))
        diaria = float(input("Valor da diaria: ").replace(",", "."))

        if noites <= 0 or diaria < 0:
            print("Digite valores validos.")
            return

    except ValueError:
        print("Digite numeros validos.")
        return

    total = noites * diaria

    reserva = {
        "hospede": hospede_encontrado["nome"],
        "quarto": quarto,
        "noites": noites,
        "diaria": diaria,
        "total": total
    }

    reservas.append(reserva)

    print("Reserva registrada com sucesso!")
    print("Hospede:", reserva["hospede"])
    print("Quarto:", quarto)
    print("Total da hospedagem: R$", round(total, 2))


def consultar_reservas():
    print("\n===== CONSULTAR RESERVAS =====")

    if len(reservas) == 0:
        print("Nenhuma reserva registrada.")
    else:
        for reserva in reservas:
            print("----------------------------")
            print("Hospede:", reserva["hospede"])
            print("Quarto:", reserva["quarto"])
            print("Noites:", reserva["noites"])
            print("Valor da diaria: R$", round(reserva["diaria"], 2))
            print("Total: R$", round(reserva["total"], 2))


def calcular_hospedagem():
    print("\n===== CALCULAR HOSPEDAGEM =====")

    try:
        noites = int(input("Quantidade de noites: "))
        diaria = float(input("Valor da diaria: R$ ").replace(",", "."))

        if noites <= 0 or diaria < 0:
            print("Digite valores validos.")
            return

        total = noites * diaria

        print("Quantidade de noites:", noites)
        print("Valor da diaria: R$", round(diaria, 2))
        print("Valor total: R$", round(total, 2))

    except ValueError:
        print("Digite numeros validos.")


def main():
    while True:
        print("\n========== HOTEL ASSOMBRADO ==========")
        print("1 - Cadastrar hospede")
        print("2 - Listar hospedes")
        print("3 - Pesquisar hospede")
        print("4 - Registrar reserva")
        print("5 - Consultar reservas")
        print("6 - Calcular hospedagem")
        print("0 - Encerrar sistema")
        print("======================================")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            cadastrar_hospede()

        elif opcao == "2":
            listar_hospedes()

        elif opcao == "3":
            pesquisar_hospede()

        elif opcao == "4":
            registrar_reserva()

        elif opcao == "5":
            consultar_reservas()

        elif opcao == "6":
            calcular_hospedagem()

        elif opcao == "0":
            print("Sistema encerrado. Obrigado por utilizar o Hotel Assombrado!")
            break

        else:
            print("Opcao invalida. Tente novamente.")


main()


