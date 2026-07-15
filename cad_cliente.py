clientes = [] # lista para guardar nome dos clientes

while True:
    print("\n=== MENU - CADASTRO DE CLIENTES ===") # o \n é uma quebra de linha.
    print("1 - Cadastrar Cliente")
    print("2 - Listar Cliente")
    print("3 - Buscar Cliente por CPF")
    print("4 - Editar Cliente")
    print("5 - Sair do Sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\t--- Iniciando cadastro ---")
        cpf = input("CPF: ") # Digitar o CPF antes de qualquer dado, evita fazer todo cadastro caso já exista #
        
        cpf_existe = False  # Começa supondo que o CPF ainda não existe#
        for cliente in clientes:
            if cliente["cpf"] == cpf:
                cpf_existe = True
                break   # Se já existir, pare. E apresente o Erro a baixo. #
        if cpf_existe:
            print(f"\nErro: já existe um cliente cadastrado com o CPF {cpf}!")   
        
        else:   # Se não existir, continue o cadastro. #
            nome = input("Digte o nome do cliente: ")
            endereco = input ("Digite endereço: ")
            telefone = input("Digite telefone: ")

            cliente = {
                "nome": nome,
                "cpf": cpf,
                "endereco": endereco,
                "telefone": telefone
            }
        
            clientes.append(cliente) #adiciona cliente cadstrdo a lista clientes
            print(f"\n Cliente cadastrado com sucesso!")

    elif opcao == "2":
        print("\n--- Lista de Clientes ---")
        if len(clientes) == 0:
            print("\nNenhum cliente cadastrado ainda!")
        else:
            for cliente in clientes:
                print(f"\nCliente:")
                print(f"\tNome: {cliente['nome']}")
                print(f"\tCPF: {cliente['cpf']}")
                print(f"\tEndereço: {cliente['endereco']}")
                print(f"\ttelefone: {cliente['telefone']}")
                print("-" * 30) #ilusão visual, dividindo um cliente do outro

    elif opcao == "3":
        cpf_busca = input("\n Digite o CPF que deseja buscar:")

        cliente_encontrado = None
        for cliente in clientes:
            if cliente["cpf"] == cpf_busca:
                cliente_encontrado = cliente
                break
        if cliente_encontrado:
            print(f"\n\t---- CLIENTE ENCONTRADO -----")
            print(f"\tNome: {cliente_encontrado ['nome']}")
            print(f"\tCPF: {cliente_encontrado ['cpf']}")
            print(f"\tEnderço: {cliente_encontrado ['endereco']}")
            print(f"\tTelefone: {cliente_encontrado['telefone']}")

        else:
            print(f"Erro: Cliente com CPF: {cpf_busca} não encontrado! ")

    elif opcao == "4":
        cpf_editar = input("Digite o CPF do cliente que deseja editar:")

        cliente_encontrado = None
        for cliente in clientes:
            if cliente["cpf"] == cpf_editar:
                cliente_encontrado = cliente
                break
        if cliente_encontrado:
            print("\t----- DADOS ATUAIS DO CLIENTE -----")
            print(f"1 - Nome: {cliente_encontrado['nome']}")
            print(f"2 - Endereço: {cliente_encontrado['endereco']}")
            print(f"3 - Telefone: {cliente_encontrado['telefone']}")
            print("( O CPF não pode ser alterado)")

            campo = input("\nDigite o número do campo que deseja alterar:")
           
            if campo == "1":
                novo_nome = input("Novo nome: ")
                cliente_encontrado["nome"] = novo_nome
                print("Nome alterado com sucesso!")

            elif campo == "2":
                novo_endereco = input("Novo Endereço: ")
                cliente_encontrado["endereco"] = novo_endereco
                print("Endereço alterado com sucesso!")

            elif campo == "3":
                novo_telefone = input("Novo nome: ")
                cliente_encontrado["telefone"] = novo_telefone
                print("Telefone alterado com sucesso!")
            else:
                print(" Opção de campo inválida")

        else:
            print(f"\n\tNenhum cliente encontrado com o CPF {cpf_editar}.")

    elif opcao == "5":
        print("Saindo do Sistema...")

    else:
        print("Opção inválida! Tente novamente.")
