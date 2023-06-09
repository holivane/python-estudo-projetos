url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
list_parametros = ['quantidade', 'moedaOrigem', 'moedaDestino']
print(url)

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_base)
print(url_parametros)

for parametro in list_parametros:
  parametro_de_busca = parametro
  indice_parametro = url_parametros.find(parametro_de_busca)
  indice_valor = indice_parametro + len(parametro_de_busca) + 1
  indice_e_comercial = url_parametros.find('&', indice_valor)
  if indice_e_comercial == -1:
      valor = url_parametros[indice_valor:]
  else:
      valor = url_parametros[indice_valor:indice_e_comercial]

  print(valor)
