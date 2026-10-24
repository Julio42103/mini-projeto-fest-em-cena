# Mini Projeto Festa em Cena - Análise de Vendas de Halloween

## Descrição

Programa em Python que lê o arquivo `halloween_vendas.csv` (1500 pedidos da loja Festa em Cena), limpa e valida os dados mostrando um resumo das vendas.

Este projeto usa apenas a biblioteca padrão do Python (`csv`, `re`, `datetime`, `collections`), sem Pandas.



## Autor
Julio Spengler - Curso Fundamentos de Programação, Dados e Machine Learning (turma 04, SCTEC)

## O arquivo de dados

O arquivo `halloween_vendas.csv` tem 1500 pedidos. Cada linha é um pedido. Exemplo (só as primeiras colunas):

`953,2025-09-05 21:16:09,Fantasia de bruxa,Fantasia,Web,Maringá,2,116.6,60.42,5,Concluído,...`

Colunas usadas no programa:

- **categoria**: tipo do produto (Fantasia ou Acessorio). Vinha com espaços, maiúsculas e texto sujo, como "  FANTASIA!!!  ".
- **canal_venda**: onde foi vendido (Web, Loja física ou Mercado). Vinha escrito de várias formas, como " loja física ".
- **quantidade**: quantas unidades foram vendidas.
- **data_venda**: data e hora da venda, usada para contar pedidos por mês.

## Regras de limpeza

- **Texto (categoria e canal_venda):** remove espaços com `strip()`, passa para minúsculas com `lower()` e tira símbolos com `re.sub`. Depois padroniza: categoria vira Fantasia ou Acessorio, e canal vira Mercado, Loja física ou Web.
- **Categoria vazia:** vira "sem categoria".
- **Quantidade:** precisa ser número inteiro maior que 0.
- **Preço unitário:** precisa estar preenchido e ser maior ou igual a 0.
- **Data da venda:** convertida com `strptime`. Se não for possível converter, o pedido é marcado como "data inválida".
- **Data de entrega:** é comparada com o status do pedido (vazia em pedido Cancelado é esperado).

## Resultados

**Total de pedidos lidos:** 1500

**Pedidos por categoria (depois da limpeza):**
- Fantasia: 979
- Acessorio: 503
- Sem categoria: 18

**Pedidos por canal de venda:**
- Web: 666
- Loja física: 551
- Mercado: 283

**Problemas encontrados nos dados:**
- preco_unitario vazio ou inválido: 12
- categoria vazia: 18
- quantidade inválida: 7
- Total de pedidos afetados: 37

**Pedidos por mês:**

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
| data inválida | 4 |

### Descobertas

1. **Outubro concentra as vendas.** Em 2024 foram 393 pedidos e em 2025 foram 410, bem mais que nos outros meses. Faz sentido por causa do Halloween.
2. **Dados inconsistentes na entrega.** Os 109 pedidos Cancelados estão sem data de entrega, como esperado. Mas 34 pedidos "Concluído" também estão sem data de entrega, o que indica falha no registro.

## Como executar

1. Baixe ou clone este repositório.
2. Deixe o arquivo `halloween_vendas.csv` na mesma pasta do `main.py`.
3. Abra o terminal na pasta do projeto e rode:

   python main.py

Para ver a checagem de data de entrega contra o status do pedido, rode:

   python checar_entrega.py

O programa precisa do Python 3 e usa só bibliotecas que já vêm com ele, então não é preciso instalar nada.

## Reflexão: qualidade de dados e Machine Learning

Um modelo de Machine Learning aprende com os dados que recebe. Se os dados vêm sujos, o modelo aprende errado ("lixo entra, lixo sai").

Neste projeto podemos ver na prática. A mesma categoria aparecia escrita de vários jeitos, como "FANTASIA!!!" e " Fantasia ". Para um modelo, isso seriam categorias diferentes. Também percebemos 18 pedidos sem categoria, 12 com preço inválido e 7 com quantidade inválida. Num cálculo de receita ou de previsão de vendas, esses erros distorceriam o resultado.

Outro caso foi a data de entrega: 34 pedidos "Concluído" não tinham data. Um modelo que tentasse prever o prazo de entrega ficaria com informação faltando.

Por isso é importante que a limpeza e a validação sejam feitas antes de qualquer modelo. Neste projeto fizemos esse primeiro passo: ler, limpar, validar e contar, para que os dados possam ser usados com confiança.

## Validação extra: datas de entrega

Foi feita uma conferência das datas de entrega (`checar_datas.py`) nos 1500 pedidos:

- 1357 pedidos foram entregues em até 30 dias depois da venda (normal).
- Nenhuma entrega aparece antes da data da venda.
- Nenhuma data veio em formato inválido.
- 143 pedidos estão sem data de entrega: 109 Cancelados (esperado) e 34 Concluídos (problema).

## Conclusão sobre pedidos sem data de entrega

Dos 1500 pedidos, 143 estão sem data de entrega. Desses, 109 são Cancelados, o que é esperado, pois um pedido cancelado não chega a ser entregue. Os outros 34 estão como Concluídos e mesmo assim não têm data de entrega, o que é uma inconsistência.

Um pedido concluído pode estar sem data de entrega por erro operacional de alguém, falha no sistema ou erro de digitação. A empresa deveria investigar esses 34 casos um a um, encontrar a causa e corrigir, para que o problema não aconteça mais.
