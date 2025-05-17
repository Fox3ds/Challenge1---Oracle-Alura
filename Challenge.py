import pandas as pd

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

loja = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)


#FATURAMENTO TOTAL

faturamento_total=[]
loja1_fat = sum(loja['Preço'])
loja2_fat = sum(loja2['Preço'])
loja3_fat = sum(loja3['Preço'])
loja4_fat = sum(loja4['Preço'])
faturamento_total.append(loja1_fat)
faturamento_total.append(loja2_fat)
faturamento_total.append(loja3_fat)
faturamento_total.append(loja4_fat)
print(faturamento_total)

#VENDAS POR CATEGORIA
cat_produtos=loja['Categoria do Produto'].unique()
print(sorted(cat_produtos))

def vends_cat (loja):
    loja_prod=dict(loja['Categoria do Produto'].value_counts())

    valor_max=max(loja_prod.values())
    
    for chave, valor in loja_prod.items():
        if valor == valor_max:
            cat_pop = {chave:valor}
            break
    

    return (loja_prod, cat_pop)

loja1_prod, cat_pop1=vends_cat(loja)
loja2_prod, cat_pop2=vends_cat(loja2)
loja3_prod, cat_pop3=vends_cat(loja3)
loja4_prod, cat_pop4=vends_cat(loja4)

print(loja1_prod, cat_pop1)

#MEDIA AVALIAÇÃO POR LOJA

def media(loja):

    media_av=round(loja['Avaliação da compra'].mean(), 2)
    return media_av

media_av1=media(loja)
media_av2=media(loja2)
media_av3=media(loja3)
media_av4=media(loja4)
media_av=[media_av1, media_av2, media_av3, media_av4]
print(media_av)

#PRODUTOS MAIS E MENOS VENDIDOS

produtos=loja['Produto'].unique()
#print(produtos)


def prod_mais(loja):

    qnt_prods=dict(loja['Produto'].value_counts())
    valor_max=max(qnt_prods.values())
    mais={}
    for chave, valor in qnt_prods.items():
        if valor == valor_max:
            mais[chave] = valor
        else:
            break
    return mais

def prod_menos(loja):

    qnt_prods=dict(loja['Produto'].value_counts())
    valor_min=min(qnt_prods.values())
    
    menos={}
    for chave, valor in reversed(qnt_prods.items()):
        if valor == valor_min:
            menos[chave] = valor
        else:
            break
    return menos

mais1 = prod_mais(loja)
menos1 = prod_menos(loja)
mais2 = prod_mais(loja2)
menos2 = prod_menos(loja2)
mais3 = prod_mais(loja3)
menos3 = prod_menos(loja3)
mais4 = prod_mais(loja4)
menos4 = prod_menos(loja4)
print(mais1, menos1)

#FRETE MEDIO POR LOJA

def frete_medio(loja):

    media_frt=round(loja['Frete'].mean(), 2)
    return media_frt

media_frt1=frete_medio(loja)
media_frt2=frete_medio(loja2)
media_frt3=frete_medio(loja3)
media_frt4=frete_medio(loja4)
media_frt=[media_frt1,media_frt2,media_frt3,media_frt4]
print(media_frt)


#GERANDO GRÁFICOS
import matplotlib.pyplot as plt

lista_lojas = ['Loja 1', 'Loja 2', 'Loja 3', 'Loja 4']
plt.figure(figsize=(8, 5))
plt.plot(lista_lojas, faturamento_total, marker='o', linestyle='-', color='royalblue', linewidth=2)
plt.title('Faturamento Total das Lojas', fontsize=14)
plt.xlabel('Lojas', fontsize=12)
plt.ylabel('Faturamento em R$', fontsize=12)
plt.ylim(1300000, 1600000)
plt.grid(True, linestyle='--', alpha=0.5)

# Adiciona os valores em cima dos pontos
for i, valor in enumerate(faturamento_total):
    plt.text(lista_lojas[i], valor + 5000, f'R$ {valor:,.2f}', ha='center', fontsize=10)

plt.tight_layout()
plt.show()




plt.figure(figsize=(8, 5))
plt.bar(lista_lojas, media_av, color='cornflowerblue')
plt.title('Média de Avaliações de Cada Loja', fontsize=14)
plt.xlabel('Lojas', fontsize=12)
plt.ylabel('Média de Avaliações', fontsize=12)
plt.ylim(3.8, 4.3)
plt.grid(axis='y', linestyle='--', alpha=0.4)

# Rótulos acima das barras
for i, valor in enumerate(media_av):
    plt.text(i, valor + 0.01, f'{valor:.2f}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()



explode = [0.1 if valor == max(media_frt) else 0 for valor in media_frt]  # Destaque para maior valor

plt.pie(media_frt, labels=lista_lojas, autopct='%1.1f%%', startangle=90, explode=explode, shadow=True)
plt.title('media do frete por loja')
plt.axis('equal')
plt.show()
