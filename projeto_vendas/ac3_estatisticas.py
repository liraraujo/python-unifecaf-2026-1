# Avaliação Continuada 3 - 1 ponto
# PROJETO DE VENDAS - parte 1
# Exercicios de estatisticas de vendas.
# Entrega - dia 17/05/2026

from banco_de_dados.conexao import conectar, fechar_conexao
from helper.validar_data import validar_data

def total_vendas_periodo():
    conexao = conectar()
    data_inicial = input('Digite a data inicial (AAAA-MM-DD): ').strip()
    data_final = input('Digite a data final (AAAA-MM-DD): ').strip()
    
    if conexao: 
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT SUM(valor_final) 
            FROM vendas 
            WHERE data_e_hora BETWEEN %s AND %s
        """, (data_inicial, data_final))
        total_vendas = cursor.fetchone()[0]

        print("\n=== TOTAL DE VENDAS NO PERÍODO ===")
        if total_vendas is not None:
            print(f"Total faturado: R$ {total_vendas:.2f}")
        else:
            print("Nenhuma venda no período informado.")

        cursor.close()
        fechar_conexao(conexao)
    return


def qtd_vendas_por_vendedor():
    conexao = conectar()
    if conexao: 
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT vendedores.nome, COUNT(vendas.id) AS qtde_vendas
            FROM vendas 
            INNER JOIN vendedores ON vendas.id_vendedor = vendedores.id
            GROUP BY vendedores.id, vendedores.nome;
        """) 
        resultados = cursor.fetchall()

        print("\n=== QUANTIDADE DE VENDAS POR VENDEDOR ===")
        if not resultados:
            print("Nenhuma venda registrada.")
        for nome, qtde in resultados:
            print(f"Vendedor: {nome} | Qtd Vendas: {qtde}")

        cursor.close()
        fechar_conexao(conexao)
    return


def ticket_medio_geral():
    # Exercicio 3: calcular o ticket medio geral a partir de vendas.valor_final.
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT AVG(valor_final) FROM vendas")
        res = cursor.fetchone()[0]
        
        print("\n=== TICKET MÉDIO GERAL ===")
        if res is not None:
            print(f"Ticket Médio: R$ {res:.2f}")
        else:
            print("Nenhuma venda cadastrada.")
            
        cursor.close()
        fechar_conexao(conexao)
    return


def ticket_medio_por_vendedor():
    # Exercicio 4: calcular o ticket medio de cada vendedor cruzando vendas e vendedores.
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT ve.nome, AVG(v.valor_final)
            FROM vendas v
            INNER JOIN vendedores ve ON v.id_vendedor = ve.id
            GROUP BY ve.id, ve.nome
        """)
        resultados = cursor.fetchall()
        
        print("\n=== TICKET MÉDIO POR VENDEDOR ===")
        if not resultados:
            print("Nenhuma venda registrada.")
        for nome, ticket_medio in resultados:
            print(f"Vendedor: {nome} | Ticket Médio: R$ {ticket_medio:.2f}")
            
        cursor.close()
        fechar_conexao(conexao)
    return


def produto_mais_vendido_qtd():
    # Exercicio 5: identificar o produto mais vendido por quantidade em vendas_produtos.
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT p.descricao, SUM(vp.quantidade) AS total_qtd
            FROM vendas_produtos vp
            INNER JOIN produtos p ON vp.id_produto = p.id
            GROUP BY p.id, p.descricao
            ORDER BY total_qtd DESC
            LIMIT 1
        """)
        res = cursor.fetchone()
        
        print("\n=== PRODUTO MAIS VENDIDO (QUANTIDADE) ===")
        if res:
            print(f"Produto: {res[0]} | Quantidade Total: {res[1]}")
        else:
            print("Nenhum produto vendido ainda.")
            
        cursor.close()
        fechar_conexao(conexao)
    return


def produto_mais_rentavel_valor():
    # Exercicio 6: identificar o produto que gerou maior faturamento somando vendas_produtos.valor_total.
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT p.descricao, SUM(vp.valor_total) AS total_faturamento
            FROM vendas_produtos vp
            INNER JOIN produtos p ON vp.id_produto = p.id
            GROUP BY p.id, p.descricao
            ORDER BY total_faturamento DESC
            LIMIT 1
        """)
        res = cursor.fetchone()
        
        print("\n=== PRODUTO MAIS RENTÁVEL (FATURAMENTO) ===")
        if res:
            print(f"Produto: {res[0]} | Faturamento Total: R$ {res[1]:.2f}")
        else:
            print("Nenhum produto vendido ainda.")
            
        cursor.close()
        fechar_conexao(conexao)
    return


def total_descontos_aplicados():
    # Exercicio 7: somar todos os descontos concedidos usando vendas.desconto.
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT SUM(desconto) FROM vendas")
        res = cursor.fetchone()[0]
        
        print("\n=== TOTAL DE DESCONTOS APLICADOS ===")
        if res is not None:
            print(f"Total de descontos: R$ {res:.2f}")
        else:
            print("Nenhuma venda registrada.")
            
        cursor.close()
        fechar_conexao(conexao)
    return


def percentual_desconto_medio():
    # Exercicio 8: calcular o percentual medio de desconto comparando desconto e valor_final das vendas.
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT AVG(desconto / (valor_final + desconto) * 100)
            FROM vendas
            WHERE (valor_final + desconto) > 0
        """)
        res = cursor.fetchone()[0]
        
        print("\n=== PERCENTUAL MÉDIO DE DESCONTO ===")
        if res is not None:
            print(f"Desconto Médio: {res:.2f}%")
        else:
            print("Nenhuma venda registrada.")
            
        cursor.close()
        fechar_conexao(conexao)
    return


def faturamento_por_dia():
    # Exercicio 9: agrupar o faturamento por dia com base em vendas.data_e_hora e vendas.valor_final.
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT DATE(data_e_hora) AS dia, SUM(valor_final) AS faturamento
            FROM vendas
            GROUP BY DATE(data_e_hora)
            ORDER BY dia ASC
        """)
        resultados = cursor.fetchall()
        
        print("\n=== FATURAMENTO POR DIA ===")
        if not resultados:
            print("Nenhuma venda registrada.")
        for dia, faturamento in resultados:
            print(f"Data: {dia} | Faturamento: R$ {faturamento:.2f}")
            
        cursor.close()
        fechar_conexao(conexao)
    return


def top_3_vendedores_faturamento():
    # Exercicio 10: listar os 3 vendedores com maior faturamento total no periodo.
    conexao = conectar()
    data_ini = input("Digite a data inicial (AAAA-MM-DD) ou Enter para geral: ").strip()
    data_fim = input("Digite a data final (AAAA-MM-DD) ou Enter para geral: ").strip()
    
    if conexao:
        cursor = conexao.cursor()
        if data_ini and data_fim:
            cursor.execute("""
                SELECT ve.nome, SUM(v.valor_final) AS faturamento
                FROM vendas v
                INNER JOIN vendedores ve ON v.id_vendedor = ve.id
                WHERE v.data_e_hora BETWEEN %s AND %s
                GROUP BY ve.id, ve.nome
                ORDER BY faturamento DESC
                LIMIT 3
            """, (data_ini, data_fim))
        else:
            cursor.execute("""
                SELECT ve.nome, SUM(v.valor_final) AS faturamento
                FROM vendas v
                INNER JOIN vendedores ve ON v.id_vendedor = ve.id
                GROUP BY ve.id, ve.nome
                ORDER BY faturamento DESC
                LIMIT 3
            """)
        resultados = cursor.fetchall()
        
        print("\n=== TOP 3 VENDEDORES POR FATURAMENTO ===")
        if not resultados:
            print("Nenhum faturamento registrado.")
        for i, (nome, faturamento) in enumerate(resultados, 1):
            print(f"{i}º Lugar: {nome} | Faturamento: R$ {faturamento:.2f}")
            
        cursor.close()
        fechar_conexao(conexao)
    return


def menu_relatorios():
    opcoes = {
        "1": ("Total de vendas por periodo", total_vendas_periodo),
        "2": ("Quantidade de vendas por vendedor", qtd_vendas_por_vendedor),
        "3": ("Ticket medio geral", ticket_medio_geral),
        "4": ("Ticket medio por vendedor", ticket_medio_por_vendedor),
        "5": ("Produto mais vendido por quantidade", produto_mais_vendido_qtd),
        "6": ("Produto mais rentavel por faturamento", produto_mais_rentavel_valor),
        "7": ("Total de descontos aplicados", total_descontos_aplicados),
        "8": ("Percentual medio de desconto", percentual_desconto_medio),
        "9": ("Faturamento por dia", faturamento_por_dia),
        "10": ("Top 3 vendedores por faturamento", top_3_vendedores_faturamento),
    }

    while True:
        print("\n=== MENU AC3 - RELATORIOS ===")
        for codigo, (descricao, _) in opcoes.items():
            print(f"{codigo} - {descricao}")
        print("0 - Voltar")

        escolha = input("Escolha uma opcao: ").strip()

        if escolha == "0":
            print("Voltando ao menu principal.")
            break

        if escolha in opcoes:
            descricao, funcao = opcoes[escolha]
            print(f"\nGerando relatorio: {descricao}")
            resultado = funcao()

            if resultado is None:
                pass
            else:
                print(resultado)
        else:
            print("Opcao invalida. Tente novamente.")
