import csv

caminho_do_arquivo = 'tracks.csv'

dados = []

with open(caminho_do_arquivo, 'r', encoding= 'utf8') as arquivo:
    arquivo_aberto = csv.DictReader(arquivo)

    for i in arquivo_aberto:
        dados.append(i)

print(dados)
