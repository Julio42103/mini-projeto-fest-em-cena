import csv
ARQUIVO = "halloween_vendas.csv"

def ler_pedidos(caminho): 
    """Lê o csv e devolve os pedidos e os nomes das colunas."""
    with open(caminho, encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        pedidos = list(leitor)
        colunas = leitor.fieldnames
    return pedidos, colunas 


pedidos, colunas = ler_pedidos(ARQUIVO)

print("Colunas:", colunas)
print("Total de linhas lidas", len(pedidos))
print("Primeiro pedido:", pedidos[0])
receita_total = 0
ignorados = 0

for pedido in pedidos:
    if pedido["status_pedido"].strip().lower() == "cancelado":
        continue

    if pedido["preco_unitario"] == "" or pedido["quantidade"] == "":
        ignorados += 1
        continue

    quantidade = int(pedido["quantidade"])
    preco = float(pedido["preco_unitario"])
    desconto = float(pedido["desconto_pct"] or 0) / 100

    receita_total += quantidade * preco * (1 - desconto)

print("Receita total:", round(receita_total, 2))
print("Pedidos ignorados por dados vazios:", ignorados)



