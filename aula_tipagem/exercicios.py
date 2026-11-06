'''Exercício 1: Filtro de Números Pares
Objetivo: Praticar iteração e manipulação de listas.

Enunciado: Escreva uma função chamada filtrar_pares(numeros) que receba uma lista de números inteiros
e retorne uma nova lista contendo apenas os números pares.

Exemplo de Entrada: [1, 2, 3, 4, 5, 6, 7, 8]

Exemplo de Saída: [2, 4, 6, 8]'''

def filtrar_pares(numeros):
    num: list[int] = []
    for i in numeros:
        if i % 2 == 0:
            num.append(i)
    print(num)

filtrar_pares([1,2,3,4,5,6,7,8])

####################################################################

""" Exercício 2: Cadastro Simples com Dicionário
Objetivo: Criação, leitura e acesso a chaves de dicionários.

Enunciado: Crie um programa que armazene os dados de um aluno (nome, idade e uma lista com três notas).
Em seguida, calcule a média das notas e adicione essa média ao dicionário sob a chave 'media'.
Ao final, exiba o dicionário completo.

Exemplo de Saída Esperada:

Python
{'nome': 'Lucas', 'idade': 17, 'notas': [7.5, 8.0, 9.5], 'media': 8.33} """

def media_aluno(nome: str, idade: int, nota1: float, nota2: float, nota3: float):
    media: float = round((nota1 + nota2 + nota3) / 3, 2)
    aluno_final = {}
    aluno_final.update({'nome': nome, 'idade': idade, 'notas': [nota1, nota2, nota3],'media': media})
    return aluno_final

print(media_aluno('Lucas', 17, 7.5, 8.0, 9.5))

####################################################################

""" Exercício 3: Frequência de Caracteres
Objetivo: Uso de dicionários como acumuladores/contadores.

Enunciado: Escreva uma função contar_caracteres(texto) que receba uma string e retorne um dicionário
indicando quantas vezes cada caractere (exceto espaços) aparece no texto.

Exemplo de Entrada: "abracadabra"

Exemplo de Saída: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1} """

def contar_caracteres(texto: str):
    saida = {}
    for i in texto:
        quantidade = texto.count(i)
        saida.update({i : quantidade})
    return saida

print(contar_caracteres("abracadabra"))

####################################################################

""" Exercício 4: Inversão de Chaves e Valores
Objetivo: Iteração sobre .items() e tratamento de colisões.

Enunciado: Crie uma função inverter_dicionario(dicionario) que inverta as chaves e os valores 
de um dicionário. Como múltiplos valores originais podem ser idênticos, os valores do novo dicionário
devem ser listas contendo todas as chaves correspondentes.

Exemplo de Entrada: {'a': 1, 'b': 2, 'c': 1, 'd': 3}

Exemplo de Saída: {1: ['a', 'c'], 2: ['b'], 3: ['d']} """

#%%
dicionario = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
invertido = {}

def inverte_dicionario(dicionario):
    invertido = {}
    for chave, valor in dicionario.items():
        if valor not in invertido:
            invertido[valor] = [chave]
        else:
            invertido[valor].append(chave)

    print(invertido)

inverte_dicionario(dicionario)


####################################################################

""" Exercício 5: Mesclagem e Consolidação de Estoques
Objetivo: Combinar múltiplos dicionários com regras de atualização.

Enunciado: Você tem duas filiais com inventários de produtos no formato {"item": quantidade}. Escreva uma função consolidar_estoques(estoque_a, estoque_b) que combine ambos os dicionários somando as quantidades de itens que aparecem em ambas as lojas.

Exemplo de Entrada:

Loja A: {"teclado": 10, "mouse": 15, "monitor": 4}

Loja B: {"mouse": 5, "fone": 12, "monitor": 2}

Exemplo de Saída:

{"teclado": 10, "mouse": 20, "monitor": 6, "fone": 12} """

####################################################################

""" Exercício 6: Agrupamento por Categoria (List of Dicts)
Objetivo: Manipular listas aninhadas e estruturas agrupadas.

Enunciado: Dada uma lista de dicionários representando produtos (cada um com 'nome', 'preco' e 'categoria'), crie uma função agrupar_por_categoria(produtos) que retorne um dicionário onde cada chave é uma categoria e o valor é uma lista apenas com os nomes dos produtos daquela categoria.

Exemplo de Entrada:

Python
[
    {"nome": "Notebook", "preco": 3500, "categoria": "Eletrônicos"},
    {"nome": "Camiseta", "preco": 60, "categoria": "Vestuário"},
    {"nome": "Mouse", "preco": 120, "categoria": "Eletrônicos"},
]
Exemplo de Saída:

Python
{
    "Eletrônicos": ["Notebook", "Mouse"],
    "Vestuário": ["Camiseta"]
} """

####################################################################

""" Exercício 7: Aplainamento de Dicionário Profundo (Flatten Dict)
Objetivo: Recursão e manipulação de árvores de chaves.

Enunciado: Crie uma função recursiva achatar_dicionario(dados, separador='.') que receba um dicionário com níveis aninhados arbitrários e o transforme em um dicionário plano de apenas um nível, concatenando as chaves aninhadas com o separador.

Exemplo de Entrada:

Python
{
    "usuario": {
        "id": 1,
        "perfil": {
            "cidade": "São Paulo",
            "ativo": True
        }
    },
    "versao": "1.0"
}
Exemplo de Saída:

Python
{
    "usuario.id": 1,
    "usuario.perfil.cidade": "São Paulo",
    "usuario.perfil.ativo": True,
    "versao": "1.0"
} """

####################################################################

""" Exercício 8: Ordenação Complexa Multinível
Objetivo: Uso avançado de sort() / sorted() com chaves customizadas (lambda ou tuplas de desempate).

Enunciado: Dada uma lista de dicionários representando atletas, ordene-os seguindo esta hierarquia:

Maior número de medalhas de ouro (decrescente)

Maior número de medalhas de prata (decrescente, para desempate)

Menor idade (crescente, para segundo desempate)

Exemplo de Entrada:

Python
[
    {"nome": "Ana", "ouro": 3, "prata": 1, "idade": 24},
    {"nome": "Carlos", "ouro": 3, "prata": 2, "idade": 28},
    {"nome": "Bia", "ouro": 3, "prata": 1, "idade": 21},
    {"nome": "Danilo", "ouro": 2, "prata": 5, "idade": 20}
]
Ordem esperada: Carlos, Bia (mais nova que Ana), Ana, Danilo. """

####################################################################

""" Exercício 9: Indexador Invertido com Stopwords
Objetivo: Algoritmos de busca textual, limpeza e estruturação de índices.

Enunciado: Escreva uma função criar_indice_remissivo(documentos, stopwords) onde documentos é uma lista de strings e stopwords é uma lista de palavras a serem desconsideradas. A função deve retornar um dicionário onde cada palavra relevante mapeia para um conjunto/lista com os índices (0, 1, 2...) dos documentos em que ela aparece (em minúsculas e sem pontuações básicas).

Exemplo de Entrada:

docs = ["Python é incrível", "Aprender Python é fácil", "Tudo é incrível"]

stopwords = ["é", "a", "tudo"]

Exemplo de Saída Esperada:

Python
{
    "python": [0, 1],
    "incrível": [0, 2],
    "aprender": [1],
    "fácil": [1]
} """


####################################################################

""" Exercício 10: Deep Diff (Comparador Estrutural de Dicionários)
Objetivo: Algoritmos de comparação estrutural e detecção de mutações.

Enunciado: Implemente uma função deep_diff(d1, d2) que compare dois dicionários arbitrários (que podem conter listas e outros dicionários) e retorne um dicionário identificando:

'adicionados': chaves presentes apenas em d2

'removidos': chaves presentes apenas em d1

'modificados': chaves com valores alterados, exibindo a tupla (valor_antigo, valor_novo)

Exemplo de Entrada:

d1 = {"a": 1, "b": [1, 2], "c": {"status": "ok"}}

d2 = {"a": 2, "b": [1, 2], "d": 99}

Exemplo de Saída Esperada:

Python
{
    "adicionados": {"d": 99},
    "removidos": {"c": {"status": "ok"}},
    "modificados": {"a": (1, 2)}
} """
# %%
