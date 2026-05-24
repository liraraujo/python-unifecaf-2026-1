# Avaliação Continuada 4 - 1 ponto
# PROJETO DE VENDAS - parte 2
# Exercicios de CRUD completo (Produtos, Vendedores e Vendas)
# Entrega - dia 24/05/2026

from banco_de_dados.conexao import conectar, fechar_conexao
from helper.validar_data import validar_data

# PRODUTOS

def criar_produto():
    conexao = conectar()
    descricao = input('Digite a descrição do produto: ')
    preco = float(input('DIgite o preço do produto: '))
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            insert into produtos (descricao, preco) values (%s, %s);
            """, (descricao, preco))
        conexao.commit()

        print("\n=== CRIAR PRODUTO ===")
        print('Produto inserido com sucesso')

        cursor.close()
        fechar_conexao(conexao)
    return

def listar_produtos():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM produtos;
        """)
        produtos = cursor.fetchall()
        print("\n=== LISTA DE PRODUTOS ===")
        for produto in produtos:
            print(produto)
        cursor.close()
        fechar_conexao(conexao)
    return


def atualizar_produto():
    conexao = conectar()
    id = input('Digite o id do produto: ')
    descricao = input('Digite a descrição do produto: ')
    preco = float(input('DIgite o preço do produto: '))

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            update produtos set descricao = %s, preco = %s where id = %s;
            """, (descricao, preco, id))
        conexao.commit()

        print("\n=== ATUALIZAR PRODUTO ===")
        print('Produto atualizado com sucesso')

        cursor.close()
        fechar_conexao(conexao)
    return


def excluir_produto():
    # Exercicio 4: excluir um produto por id, tratando dependencias em vendas_produtos.
    conexao = conectar()
    id = input('Digite o id do produto a ser excluído: ').strip()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM vendas_produtos WHERE id_produto = %s", (id,))
        cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
        conexao.commit()
        
        print("\n=== EXCLUIR PRODUTO ===")
        print('Produto e suas dependências excluídos com sucesso.')
        
        cursor.close()
        fechar_conexao(conexao)
    return


# VENDEDORES

def criar_vendedor():
    # Exercicio 5: cadastrar um novo vendedor na tabela vendedores.
    conexao = conectar()
    nome = input('Digite o nome do vendedor: ').strip()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO vendedores (nome) VALUES (%s)", (nome,))
        conexao.commit()
        
        print("\n=== CRIAR VENDEDOR ===")
        print('Vendedor cadastrado com sucesso.')
        
        cursor.close()
        fechar_conexao(conexao)
    return


def listar_vendedores():
    # Exercicio 6: listar todos os vendedores cadastrados.
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome FROM vendedores")
        vendedores = cursor.fetchall()
        
        print("\n=== LISTA DE VENDEDORES ===")
        if not vendedores:
            print("Nenhum vendedor cadastrado.")
        for vendedor in vendedores:
            print(f"ID: {vendedor[0]} | Nome: {vendedor[1]}")
            
        cursor.close()
        fechar_conexao(conexao)
    return


def atualizar_vendedor():
    # Exercicio 7: atualizar o nome de um vendedor existente por id.
    conexao = conectar()
    id = input('Digite o id do vendedor: ').strip()
    nome = input('Digite o novo nome do vendedor: ').strip()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("UPDATE vendedores SET nome = %s WHERE id = %s", (nome, id))
        conexao.commit()
        
        print("\n=== ATUALIZAR VENDEDOR ===")
        print('Vendedor atualizado com sucesso.')
        
        cursor.close()
        fechar_conexao(conexao)
    return


def excluir_vendedor():
    # Exercicio 8: excluir vendedor por id, validando se possui vendas vinculadas.
    conexao = conectar()
    id = input('Digite o id do vendedor a ser excluído: ').strip()
    if conexao:
        cursor = conexao.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM vendas WHERE id_vendedor = %s", (id,))
        total_vendas = cursor.fetchone()[0]
        
        print("\n=== EXCLUIR VENDEDOR ===")
        if total_vendas > 0:
            print(f"Erro: Não é possível excluir o vendedor. Ele possui {total_vendas} venda(s) vinculada(s).")
        else:
            cursor.execute("DELETE FROM vendedores WHERE id = %s", (id,))
            conexao.commit()
            print('Vendedor excluído com sucesso.')
            
        cursor.close()
        fechar_conexao(conexao)
    return


# VENDAS

def criar_venda_com_itens():
    # Exercicio 9: criar uma venda e inserir itens na tabela vendas_produtos com quantidade e valores.
    from datetime import datetime
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        
        id_vendedor = input('Digite o ID do vendedor: ').strip()
        data_e_hora_input = input('Digite a data e hora (AAAA-MM-DD HH:MM:SS) ou pressione Enter para usar a hora atual: ').strip()
        if not data_e_hora_input:
            data_e_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        else:
            data_e_hora = data_e_hora_input
            
        desconto = float(input('Digite o valor do desconto (ou 0): ').strip() or 0)
        
        itens = []
        print("\n--- Adicionar Itens à Venda ---")
        while True:
            id_produto = input("Digite o ID do produto (ou '0' para finalizar): ").strip()
            if id_produto == '0' or not id_produto:
                break
            
            cursor.execute("SELECT preco FROM produtos WHERE id = %s", (id_produto,))
            res_prod = cursor.fetchone()
            if not res_prod:
                print("Produto não encontrado! Tente novamente.")
                continue
            
            preco_sugerido = res_prod[0]
            print(f"Preço do produto cadastrado: R$ {preco_sugerido:.2f}")
            
            quantidade = int(input("Digite a quantidade: "))
            valor_unitario_input = input(f"Digite o valor unitário (Enter para R$ {preco_sugerido:.2f}): ").strip()
            
            if not valor_unitario_input:
                valor_unitario = float(preco_sugerido)
            else:
                valor_unitario = float(valor_unitario_input)
                
            valor_total = quantidade * valor_unitario
            itens.append((id_produto, quantidade, valor_unitario, valor_total))
            print(f"Item adicionado: Total de R$ {valor_total:.2f}")
            
        if not itens:
            print("Nenhum item adicionado. Venda cancelada.")
            cursor.close()
            fechar_conexao(conexao)
            return
            
        soma_itens = sum(item[3] for item in itens)
        valor_final = max(0.0, soma_itens - desconto)
        
        cursor.execute("""
            INSERT INTO vendas (id_vendedor, data_e_hora, desconto, valor_final)
            VALUES (%s, %s, %s, %s)
        """, (id_vendedor, data_e_hora, desconto, valor_final))
        
        id_venda = cursor.lastrowid
        
        for id_produto, quantidade, valor_unitario, valor_total in itens:
            cursor.execute("""
                INSERT INTO vendas_produtos (id_venda, id_produto, quantidade, valor_unitario, valor_total)
                VALUES (%s, %s, %s, %s, %s)
            """, (id_venda, id_produto, quantidade, valor_unitario, valor_total))
            
        conexao.commit()
        print("\n=== CRIAR VENDA COM ITENS ===")
        print(f"Venda registrada com sucesso! ID da venda: {id_venda}. Valor final: R$ {valor_final:.2f}")
        
        cursor.close()
        fechar_conexao(conexao)
    return


def listar_vendas_completas():
    # Exercicio 10: listar vendas com vendedor e itens (produto, quantidade, valor_unitario, valor_total).
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        
        cursor.execute("""
            SELECT v.id, vd.nome, v.data_e_hora, v.desconto, v.valor_final
            FROM vendas v
            INNER JOIN vendedores vd ON v.id_vendedor = vd.id
            ORDER BY v.id DESC
        """)
        vendas = cursor.fetchall()
        
        print("\n=== LISTA DE VENDAS COMPLETAS ===")
        if not vendas:
            print("Nenhuma venda registrada.")
        
        for venda in vendas:
            id_venda, nome_vendedor, data_e_hora, desconto, valor_final = venda
            print("-" * 50)
            print(f"Venda ID: {id_venda} | Vendedor: {nome_vendedor} | Data: {data_e_hora}")
            print(f"Desconto: R$ {desconto:.2f} | Valor Final: R$ {valor_final:.2f}")
            print("  Itens da Venda:")
            
            cursor.execute("""
                SELECT p.descricao, vp.quantidade, vp.valor_unitario, vp.valor_total
                FROM vendas_produtos vp
                INNER JOIN produtos p ON vp.id_produto = p.id
                WHERE vp.id_venda = %s
            """, (id_venda,))
            itens = cursor.fetchall()
            
            for item in itens:
                descricao, quantidade, valor_unitario, valor_total = item
                print(f"    - {descricao} | Qtd: {quantidade} | Unitário: R$ {valor_unitario:.2f} | Total: R$ {valor_total:.2f}")
        print("-" * 50)
        
        cursor.close()
        fechar_conexao(conexao)
    return


def atualizar_venda_e_itens():
    # Exercicio 11: atualizar dados da venda (desconto/valor_final) e seus itens.
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        
        id_venda = input('Digite o ID da venda que deseja atualizar: ').strip()
        
        cursor.execute("SELECT desconto, valor_final FROM vendas WHERE id = %s", (id_venda,))
        res_venda = cursor.fetchone()
        if not res_venda:
            print("Venda não encontrada!")
            cursor.close()
            fechar_conexao(conexao)
            return
            
        desc_atual, valor_atual = res_venda
        print(f"Venda encontrada! Desconto atual: R$ {desc_atual:.2f} | Valor final atual: R$ {valor_atual:.2f}")
        
        novo_desconto_input = input(f"Digite o novo valor de desconto (Enter para manter R$ {desc_atual:.2f}): ").strip()
        novo_desconto = float(novo_desconto_input) if novo_desconto_input else float(desc_atual)
        
        atualizar_itens = input("Deseja redefinir os itens desta venda? (s/n): ").strip().lower()
        
        if atualizar_itens == 's':
            itens = []
            print("\n--- Redefinir Itens da Venda ---")
            while True:
                id_produto = input("Digite o ID do produto (ou '0' para finalizar): ").strip()
                if id_produto == '0' or not id_produto:
                    break
                
                cursor.execute("SELECT preco FROM produtos WHERE id = %s", (id_produto,))
                res_prod = cursor.fetchone()
                if not res_prod:
                    print("Produto não encontrado! Tente novamente.")
                    continue
                
                preco_sugerido = res_prod[0]
                print(f"Preço do produto cadastrado: R$ {preco_sugerido:.2f}")
                
                quantidade = int(input("Digite a quantidade: "))
                valor_unitario_input = input(f"Digite o valor unitário (Enter para R$ {preco_sugerido:.2f}): ").strip()
                
                if not valor_unitario_input:
                    valor_unitario = float(preco_sugerido)
                else:
                    valor_unitario = float(valor_unitario_input)
                    
                valor_total = quantidade * valor_unitario
                itens.append((id_produto, quantidade, valor_unitario, valor_total))
                
            if itens:
                cursor.execute("DELETE FROM vendas_produtos WHERE id_venda = %s", (id_venda,))
                for id_produto, quantidade, valor_unitario, valor_total in itens:
                    cursor.execute("""
                        INSERT INTO vendas_produtos (id_venda, id_produto, quantidade, valor_unitario, valor_total)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (id_venda, id_produto, quantidade, valor_unitario, valor_total))
                    
                soma_itens = sum(item[3] for item in itens)
                valor_final = max(0.0, soma_itens - novo_desconto)
            else:
                print("Nenhum item inserido. Os itens anteriores da venda não foram modificados.")
                cursor.execute("SELECT SUM(valor_total) FROM vendas_produtos WHERE id_venda = %s", (id_venda,))
                soma_itens = cursor.fetchone()[0] or 0.0
                valor_final = max(0.0, float(soma_itens) - novo_desconto)
        else:
            cursor.execute("SELECT SUM(valor_total) FROM vendas_produtos WHERE id_venda = %s", (id_venda,))
            soma_itens = cursor.fetchone()[0] or 0.0
            valor_final = max(0.0, float(soma_itens) - novo_desconto)
            
        cursor.execute("""
            UPDATE vendas SET desconto = %s, valor_final = %s WHERE id = %s
        """, (novo_desconto, valor_final, id_venda))
        
        conexao.commit()
        print("\n=== ATUALIZAR VENDA E ITENS ===")
        print(f"Venda atualizada com sucesso! Novo valor final: R$ {valor_final:.2f}")
        
        cursor.close()
        fechar_conexao(conexao)
    return


def excluir_venda():
    # Exercicio 12: excluir uma venda por id removendo primeiro os itens de vendas_produtos.
    conexao = conectar()
    id_venda = input('Digite o ID da venda que deseja excluir: ').strip()
    if conexao:
        cursor = conexao.cursor()
        
        cursor.execute("SELECT id FROM vendas WHERE id = %s", (id_venda,))
        if not cursor.fetchone():
            print("Venda não encontrada!")
            cursor.close()
            fechar_conexao(conexao)
            return
            
        cursor.execute("DELETE FROM vendas_produtos WHERE id_venda = %s", (id_venda,))
        cursor.execute("DELETE FROM vendas WHERE id = %s", (id_venda,))
        conexao.commit()
        
        print("\n=== EXCLUIR VENDA ===")
        print("Venda e seus itens excluídos com sucesso.")
        
        cursor.close()
        fechar_conexao(conexao)
    return


def menu():
    opcoes = {
        "1": ("Criar produto", criar_produto),
        "2": ("Listar produtos", listar_produtos),
        "3": ("Atualizar produto", atualizar_produto),
        "4": ("Excluir produto", excluir_produto),
        "5": ("Criar vendedor", criar_vendedor),
        "6": ("Listar vendedores", listar_vendedores),
        "7": ("Atualizar vendedor", atualizar_vendedor),
        "8": ("Excluir vendedor", excluir_vendedor),
        "9": ("Criar venda com itens", criar_venda_com_itens),
        "10": ("Listar vendas completas", listar_vendas_completas),
        "11": ("Atualizar venda e itens", atualizar_venda_e_itens),
        "12": ("Excluir venda", excluir_venda),
    }

    while True:
        print("\n=== MENU AC4 - CRUD COMPLETO ===")
        for codigo, (descricao, _) in opcoes.items():
            print(f"{codigo} - {descricao}")
        print("0 - Voltar")

        escolha = input("Escolha uma opcao: ").strip()

        if escolha == "0":
            print("Voltando ao menu principal.")
            break

        if escolha in opcoes:
            descricao, funcao = opcoes[escolha]
            print(f"\nSelecionado: {descricao}")
            funcao()
            print("Exercicio em estrutura base (return vazio).")
        else:
            print("Opcao invalida. Tente novamente.")


menu()