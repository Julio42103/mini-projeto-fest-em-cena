# Relatório: Análise de Vendas de Halloween (Festa em Cena)

## Objetivo

Limpar, validar e resumir os dados de 1500 pedidos da loja Festa em Cena (arquivo `halloween_vendas.csv`), usando apenas Python (`csv`, `re`, `datetime`, `collections`), sem Pandas.

## Resultados

**Pedidos por categoria (depois da limpeza)**
- Fantasia: 979
- Acessório: 503
- Sem categoria: 18

**Pedidos por canal de venda**
- Web: 666
- Loja física: 551
- Mercado: 283

**Problemas encontrados nos dados**
- Preço unitário vazio ou inválido: 12
- Categoria vazia: 18
- Quantidade inválida: 7
- Total de pedidos afetados: 37

**Pedidos por mês**

| Mês | Pedidos |
|---|---|
| 2024-08 | 77 |
| 2024-09 | 104 |
| 2024-10 | 393 |
| 2024-11 | 174 |
| 2025-08 | 62 |
| 2025-09 | 94 |
| 2025-10 | 410 |
| 2025-11 | 182 |
| Data inválida | 4 |

**Datas de entrega**
- 1357 pedidos foram entregues em até 30 dias depois da venda.
- Nenhuma entrega aparece antes da data da venda.
- 143 pedidos estão sem data de entrega: 109 Cancelados (esperado) e 34 Concluídos (problema).

## Interpretações

**Descoberta 1: outubro concentra as vendas.** As vendas são sazonais e crescem muito perto do Halloween: 393 pedidos em outubro de 2024 e 410 em outubro de 2025, bem mais que nos outros meses.

**Descoberta 2: dados inconsistentes na entrega.** 34 pedidos Concluídos estão sem data de entrega, o que indica falha no registro dos dados.

## Limitações

- O arquivo só tem os meses de agosto a novembro, de dois anos. Não dá para saber como foram as vendas nos outros meses, então não é possível fazer uma análise mais aprofundada das vendas ao longo do ano.
- Os dados mostram que a data de entrega está faltando, mas não mostram o motivo. Pedidos sem data de entrega podem dificultar o faturamento e precisam ser investigados.

## Tratamento dos valores nulos

Os pedidos com problemas não foram apagados, pois cada um é um pedido real e apagá-los mudaria o total de 1500 e faria perder informações dos outros campos. Também não foi inventado nenhum valor, pois chutar um valor distorceria os resultados e tiraria a confiabilidade da análise. A categoria vazia foi marcada como "sem categoria" e os problemas de preço e quantidade foram contados e relatados.

## Conclusão

A limpeza e a validação dos dados mostraram que o arquivo tinha 37 pedidos com problemas e 34 pedidos Concluídos sem data de entrega. A empresa deveria investigar esses casos um a um, encontrar a causa e corrigir, para que o problema não aconteça mais. Esse trabalho precisa ser feito antes de usar os dados em qualquer relatório de faturamento ou modelo de Machine Learning.
