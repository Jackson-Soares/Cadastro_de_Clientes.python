'''criar um sistema de vendas:
cadastrar produtos e cliente; estoque; vendas;
contas a pagar e receber; painel de controle'''

estoque_de_produtos= {}

while True:
    print("\n=== MENU - CADASTRO DE PRODUTOS ===") # o \n é uma quebra de linha.
    print("1 - Cadastrar Produto")
    print("2 - Listar Produto")
    print("3 - Buscar Produto por descrição")
    print("4 - Editar Produto")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\t--- Iniciando cadastro ---")
        codigo = input("Código de barras: ").strip() # Digitar o Código antes de qualquer dado, evita fazer todo cadastro caso já exista #
        if codigo in estoque_de_produtos:
            print(f"\nErro: Já existe um produto cadastrado com este Código!")   
        
        else:   # Se não existir, continue o cadastro. #
            descricao = input("Descrição do Produto: ").strip()
            preco_texto = input ("Preço: ")
            preco_texto = preco_texto.replace("," , ".")
            preco_texto = float(preco_texto)
            estoque = int (input ("Estoque: "))
            indicacao = input ("Indicação: ")
            posologia = input ("Posologia: ")
            contraindicacao = input("Contraindicações: ")

            produto = {
                "descricao": descricao,
                "preco": preco_texto,
                "estoque": estoque,
                "indicacao": indicacao,
                "posologia" : posologia,
                "contraindicacao" : contraindicacao,
            }
        
            estoque_de_produtos[codigo] = produto #adiciona produto cadastrado ao dicionário cadastro_de_produtos
            print(f"\n Produto cadastrado com sucesso!")

