import csv
from collections import Counter

contagem = Counter()

with open("halloween_vendas.csv", encoding="utf-8") as f:
    for pedido in csv.DictReader(f):
        status = pedido["status_pedido"].strip().lower()
        sem_entrega = pedido["data_entrega"].strip() == ""
        contagem[(status, sem_entrega)] += 1

for (status, sem_entrega), qtd in sorted(contagem.items()):
    print(f"status={status} | data_entrega vazia={sem_entrega}: {qtd}")

