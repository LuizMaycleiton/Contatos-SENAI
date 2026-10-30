import sqlite3

def conexao_banco():
    conexao = sqlite3.connect("contatos.db")
    cursor = conexao.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL
    );'''
    cursor.execute(sql)
    conexao.commit()
    return conexao

def adicionar_contato(nome, telefone, email):
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''
    INSERT INTO contatos (nome, telefone, email)
    VALUES (?, ?, ?)'''
    cursor.execute(sql, (nome, telefone, email))
    conexao.commit()
    conexao.close()
    print("Contato adicionado com sucesso!\n")

def listar_contatos():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM contatos"
    cursor.execute(sql)
    contatos = cursor.fetchall()
    conexao.close()

    print("\n### LISTA DE CONTATOS ###")
    print(f"{'id':<5} | {'nome':<20} | {'telefone':<15} | {'email':<30}")
    print("-" * 79)
    for contato in contatos:
        print(f"{contato[0]:<5} | {contato[1]:<20} | {contato[2]:<15} | {contato[3]:<30}")
    print("\n")

def buscar_contato(nome_busca):
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM contatos WHERE nome LIKE ?"
    cursor.execute(sql, ('%' + nome_busca + '%',))
    contatos = cursor.fetchall()
    conexao.close()

    if not contatos:
        print("Nenhum contato encontrado com esse nome.\n")
        return

    print("\n### RESULTADO DA BUSCA ###")
    print(f"{'id':<5} | {'nome':<20} | {'telefone':<15} | {'email':<30}")
    print("-" * 79)
    for contato in contatos:
        print(f"{contato[0]:<5} | {contato[1]:<20} | {contato[2]:<15} | {contato[3]:<30}")
    print("\n")

def atualizar_contato(id_contato, nome, telefone, email):
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''
    UPDATE contatos 
    SET nome = ?, telefone = ?, email = ? 
    WHERE id = ?'''
    cursor.execute(sql, (nome, telefone, email, id_contato))
    conexao.commit()
    conexao.close()
    print("Contato atualizado com sucesso!\n")

def excluir_contato(id_contato):
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM contatos WHERE id = ?"
    cursor.execute(sql, (id_contato,))
    conexao.commit()
    conexao.close()
    print("Contato excluído com sucesso!\n")

conexao_banco().close()

while True:
    print("### CONTATOS ###")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Buscar contato pelo nome")
    print("4. Atualizar contato")
    print("5. Excluir contato")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        adicionar_contato(nome, telefone, email)
        
    elif opcao == "2":    
        listar_contatos()
        
    elif opcao == "3":
        nome_busca = input("Digite o nome para buscar: ")
        buscar_contato(nome_busca)
        
    elif opcao == "4":
        listar_contatos()
        try:
            id_contato = int(input("Digite o ID do contato que deseja atualizar: "))
            nome = input("Novo Nome: ")
            telefone = input("Novo Telefone: ")
            email = input("Novo Email: ")
            atualizar_contato(id_contato, nome, telefone, email)
        except ValueError:
            print("Por favor, digite um ID numérico válido.\n")
            
    elif opcao == "5":
        listar_contatos()
        try:
            id_contato = int(input("Digite o ID do contato que deseja excluir: "))
            excluir_contato(id_contato)
        except ValueError:
            print("Por favor, digite um ID numérico válido.\n")
            
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.\n")