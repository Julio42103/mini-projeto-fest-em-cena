import csv
import re
from collections import Counter
ARQUIVO = "halloween_vendas.csv"

def limpar_categoria(texto): 
    texto = texto.strip().lower()
    texto = re.sub(r"[^a-z]", "",texto)
    if texto =="":
        return "sem categoria"    
    return texto.capitalize()

def limpar_canal(texto):
    texto = texto.strip().lower()
    nomes = {"web": "Web", "loja física": "Loja física", "mercado": "Mercado"}
    return nomes.get(texto, texto)

def problemas_do_pedido(pedido):
    problemas = []
    if pedido["categoria"] == "sem categoria":
        problemas.append("categoria")
    try:
        if int(pedido["quantidade"]) <= 0:

            problemas.append("quantidade")
    except ValueError:
        problemas.append("quantidade")
    try:
        if float(pedido["preco_unitario"]) < 0:

            problemas.append("preco_unitario")
    except ValueError:

        problemas.append("preco_unitario")
    return problemas

def ler_pedidos(caminho): 
    """Lê o csv e devolve os pedidos e os nomes das colunas."""
    with open(caminho, encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        pedidos = list(leitor)
        colunas = leitor.fieldnames
    return pedidos, colunas 


pedidos, colunas = ler_pedidos(ARQUIVO)

for pedido in pedidos:
    pedido["categoria"] = limpar_categoria(pedido["categoria"])
    pedido["canal_venda"] = limpar_canal(pedido["canal_venda"])
print("Colunas:", colunas)
print("Total de Linhas Lidas:", len(pedidos))
print("Três primeiros pedidos:")
for pedido in pedidos[:3]:
    print(pedido)

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
print(Counter(p["categoria"] for p in pedidos))
print(Counter(p["canal_venda"] for p in pedidos))

contagem = Counter()
afetados = 0
for pedido in pedidos:
    problemas = problemas_do_pedido(pedido)
    if problemas:
        afetados += 1
    for campo in problemas:
        contagem[campo] += 1

print("Problemas por campo:", dict(contagem))
print("Pedidos afetados:", afetados)

