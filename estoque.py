# sistema simples de controle de estoque
estoque = {}

# mostra o menu principal
def menu():
    print("\n=== MENU ===")
    print("[1] Adicionar produto")
    print("[2] Atualizar produto")
    print("[3] Excluir produto")
    print("[4] Ver estoque")
    print("[0] Sair")

# adiciona produto no estoque
def adicionar_produto():
    nome = input("Nome do produto: ").strip().lower()

    # verifica se digitou algo
    if nome == "":
        print("Nome inválido")
        return

    try:
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Valor inválido")
        return

    # se já existir, soma a quantidade
    if nome in estoque:
        estoque[nome]["quantidade"] += quantidade
        print(f"Produto já existia, quantidade atualizada para {estoque[nome]['quantidade']}")
    else:
        # cria produto novo
        estoque[nome] = {
            "preco": preco,
            "quantidade": quantidade
        }
        print(f"Produto {nome} cadastrado com sucesso")

# atualiza preço ou quantidade
def atualizar_produto():
    nome = input("Nome do produto: ").strip().lower()

    # verifica se existe
    if nome not in estoque:
        print(f"Produto {nome} não existe")
        return

    print("[1] Atualizar preço")
    print("[2] Atualizar quantidade")
    opcao = input("Opção: ")

    try:
        if opcao == "1":
            novo_preco = float(input("Novo preço: "))
            estoque[nome]["preco"] = novo_preco
            print(f"Preço do produto {nome} atualizado")
        elif opcao == "2":
            nova_quantidade = int(input("Nova quantidade: "))
            estoque[nome]["quantidade"] = nova_quantidade
            print(f"Quantidade do produto {nome} atualizada")
        else:
            print("Opção inválida")
    except ValueError:
        print("Valor inválido")

# remove produto do estoque
def excluir_produto():
    nome = input("Nome do produto: ").strip().lower()

    if nome in estoque:
        del estoque[nome]
        print(f"Produto {nome} removido")
    else:
        print(f"Produto {nome} não encontrado")

# visualiza o estoque
def visualizar_estoque():
    print("\n[1] Ver todos os produtos")
    print("[2] Buscar produto por nome")
    print("[3] Voltar")

    opcao = input("Opção: ")

    # mostra todos
    if opcao == "1":
        if not estoque:
            print("Estoque vazio")
            return

        print("\n--- ESTOQUE ---")
        for nome, dados in estoque.items():
            print(f"Produto: {nome}")
            print(f"Preço: R$ {dados['preco']}")
            print(f"Quantidade: {dados['quantidade']}")
            print("--------------")

    # busca um produto
    elif opcao == "2":
        nome = input("Nome do produto: ").strip().lower()

        if nome in estoque:
            print("\n--- PRODUTO ---")
            print(f"Produto: {nome}")
            print(f"Preço: R$ {estoque[nome]['preco']}")
            print(f"Quantidade: {estoque[nome]['quantidade']}")
        else:
            print(f"Produto {nome} não encontrado")

    elif opcao == "3":
        return
    else:
        print("Opção inválida")

# laço principal
while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        atualizar_produto()
    elif opcao == "3":
        excluir_produto()
    elif opcao == "4":
        visualizar_estoque()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida")