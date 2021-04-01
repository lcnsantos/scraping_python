#Código de um web scraper simples em Python par coletar links, palavras ou frases
#Mude o link na linha 8 para estudar um site diferente

import urllib.request
import codecs

#Parte do código para ler um site
fp = urllib.request.urlopen('http://globo.com')
mybytes = fp.read()
data1 = mybytes.decode("utf8",errors='ignore')
fp.close()
teste=str(data1)
data2 = data1.split()

#Função para procurar links na lista data2 - Para procurar um padrão diferente, alterar as condições nos if's
lista1 = data2
lista2 = []

for key in lista1:
    if(key.find('http://' or 'https://')!=-1):
        inicio = key.find('http')
        if(key.find('">')!=-1):
            fim = key.find('">')
            palavra = key[inicio:fim ]
            lista2.append(palavra)
# Opção para imprimir os dados coletados --> print(lista2)

#Lendo a lista2 com o Pandas
import pandas as dados
df=dados.DataFrame(lista2)
print(df.head(50))

#salvando os dados em csv
df.to_csv("dados_coletados.csv")

