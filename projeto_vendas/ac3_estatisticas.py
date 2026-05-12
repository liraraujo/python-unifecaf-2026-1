# Avaliação Continuada 3 - 1 ponto
# PROJETO DE VENDAS - parte 1
# Exercicios de estatisticas de vendas.
# Entrega - dia 17/05/2026

from banco_de_dados.conexao import conectar, fechar_conexao
from helper.validar_data import validar_data

def total_vendas_periodo():
    conexao = conectar()

    data_inicial = input('Digite a data inicial (YYYY-mm-dd):')
    while not validar_data:
        print('Data inválida, tente novamente!')
        data_inicial = input('Digite a data inicial (YYYY-mm-dd):')

    data_final = input('Digite a data final (YYYY-mm-dd):')
    while not validar_data:
        print('Data inválida, tente novamente!')
        data_inicial = input('Digite a data inicial (YYYY-mm-dd):')
    
    if conexao: 
        cursor = conexao.cursor
        cursor.execute("""
         select sum(valor_final) 
         from vendas 
         where data_e_hora between %s and %s
        
        """, (data_inicial, data_final))
        total_vendas = cursor.fetchone()

        print("\n=== LISTA DE TOTAL DE VENDAS ===")
        print(f"Total: {total_vendas }")

        cursor.close()
        fechar_conexao(conexao)


def qtd_vendas_por_vendedor():
    conexao = conectar()
     
    if conexao: 
        cursor = conexao.cursor
        cursor.execute("""
        select vendedores.nome, count(*)qtde_vendas
        from vendas 
        inner join vendedores
	    on vendas.id_vendedor = vendedores.id
        group by vendedores.id;
        
        """) 
    return


def ticket_medio_geral():
    # Exercicio 3: calcular o ticket medio geral a partir de vendas.valor_final.
    return


def ticket_medio_por_vendedor():
    # Exercicio 4: calcular o ticket medio de cada vendedor cruzando vendas e vendedores.
    return


def produto_mais_vendido_qtd():
    # Exercicio 5: identificar o produto mais vendido por quantidade em vendas_produtos.
    return


def produto_mais_rentavel_valor():
    # Exercicio 6: identificar o produto que gerou maior faturamento somando vendas_produtos.valor_total.
    return


def total_descontos_aplicados():
    # Exercicio 7: somar todos os descontos concedidos usando vendas.desconto.
    return


def percentual_desconto_medio():
    # Exercicio 8: calcular o percentual medio de desconto comparando desconto e valor_final das vendas.
    return


def faturamento_por_dia():
    # Exercicio 9: agrupar o faturamento por dia com base em vendas.data_e_hora e vendas.valor_final.
    return


def top_3_vendedores_faturamento():
    # Exercicio 10: listar os 3 vendedores com maior faturamento total no periodo.
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
                print("Relatorio em estrutura base (return vazio).")
            else:
                print(resultado)
        else:
            print("Opcao invalida. Tente novamente.")
