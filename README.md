📊 Análise de Desempenho de Lojas Virtuais
Este projeto tem como objetivo analisar e comparar o desempenho de quatro lojas virtuais a partir de dados reais de vendas. A análise foi feita como parte de um desafio de ciência de dados da Alura e busca responder à pergunta: qual loja o dono deveria vender?

🔍 Sobre o Projeto
Utilizando dados disponíveis em arquivos CSV hospedados no GitHub, o código realiza uma série de análises e visualizações para apoiar a tomada de decisão. São avaliados os seguintes aspectos:

Faturamento total por loja

Média das avaliações dos clientes

Produtos mais e menos vendidos

Categoria de produto mais popular

Frete médio por loja

Visualizações com gráficos de linha, barras e pizza

🛠️ Tecnologias Utilizadas
Python

Pandas

Matplotlib

Jupyter Notebook (ou Google Colab)

📁 Fontes dos Dados
Os dados foram obtidos diretamente dos arquivos CSV hospedados no GitHub da Alura:

Loja 1: loja_1.csv

Loja 2: loja_2.csv

Loja 3: loja_3.csv

Loja 4: loja_4.csv

Os arquivos são carregados diretamente a partir das seguintes URLs:

python
Copiar
Editar
url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
(E assim por diante para as demais lojas)

📊 Etapas da Análise
Leitura dos dados CSV
Carregamento dos dados de cada loja usando a biblioteca pandas.

Faturamento total por loja
Soma dos valores de venda de cada loja.

Média das avaliações
Cálculo da média de satisfação dos clientes para cada loja.

Análise por categoria
Identificação da categoria mais vendida em cada loja.

Produtos mais e menos vendidos
Contagem de ocorrência de cada produto e identificação dos extremos.

Frete médio
Cálculo do valor médio de frete praticado em cada loja.

Visualizações
Gráficos de:

Faturamento total

Média das avaliações

Participação percentual do frete médio

📌 Conclusões
A análise sugere que a Loja 4 é a que apresenta pior desempenho geral, tendo o menor faturamento, avaliações medianas e desempenho fraco nas vendas. Logo, ela é a recomendada para ser vendida, permitindo ao dono focar em lojas com maior potencial, como a Loja 1 e a Loja 3.

📷 Exemplos de Gráficos Gerados
Linha de faturamento por loja

Barras de média de avaliação

Gráfico de pizza com comparação do frete médio
