#url = " bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url = " "

#Sanitização da URL
url = url.strip(" ", "")



# Validação da Url
if url == "":
    raise ValueError("A URL está vazia")

# Separa a base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametro = url[indice_interrogacao + 1:]
print(url_parametro)

# Busca valor de um parâmetro
parametro_de_busca = 'quantidade'
indice_parametro = url_parametro.find(parametro_de_busca)
indice_valor = indice_parametro + len(parametro_de_busca) + 1
indice_e_comercial = url_parametro.find('&', indice_valor)
if indice_valor == -1:
    valor = url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]
print(valor)
