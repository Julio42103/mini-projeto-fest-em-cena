import csv
from datetime import datetime

formato = "%Y-%m-%d %H:%M:%S"
antes = 0
normal = 0
muito_depois = 0
sem_data = 0
invalidas = 0

with open("halloween_vendas.csv", encoding="utf-8") as f:
    for pedido in csv.DictReader(f):
        entrega_txt = pedido["data_entrega"].strip()
        if entrega_txt == "":
            sem_data += 1
            continue
        try:
            venda = datetime.strptime(pedido["data_venda"].strip(), formato)
            entrega = datetime.strptime(entrega_txt, formato)
        except ValueError:
            invalidas += 1
            continue
        dias = (entrega - venda).days
        if dias < 0:
            antes += 1
        elif dias <= 30:
            normal += 1
        else:
            muito_depois += 1

print("Sem data de entrega:", sem_data)
print("Data inválida:", invalidas)
print("Entrega ANTES da venda:", antes)
print("Entrega até 30 dias depois (normal):", normal)
print("Entrega mais de 30 dias depois:", muito_depois)

