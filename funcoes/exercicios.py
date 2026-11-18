#%%
#Cálculo de Desconto

# Crie uma função chamada calcular_desconto que receba dois parâmetros: preco (float) e percentual (float).
# A função deve retornar o valor final do produto com o desconto aplicado.
# Exemplo de entrada: calcular_desconto(100, 15)
# Saída esperada: 85.0


def calcular_desconto(preco: float, desconto: float) -> float:
    valor_final = preco - (preco*desconto/100)
    return valor_final

calcular_desconto(100,15)
# %%
# 2. Verificador de Palíndromos (Nível: Iniciante)
# Escreva uma função chamada eh_palindromo que receba uma palavra ou frase (string) e retorne True se ela for um palíndromo (lê-se igual de trás para frente) ou False caso contrário.

# Dica: Ignore espaços em branco e letras maiúsculas/minúsculas.

# Exemplo de entrada: eh_palindromo("Ame a ema")


def e_palindromo(palavra: str) -> str:
    palavra_invertida = ''
    for i in range(len(palavra)-1, -1, -1):
        palavra_invertida = palavra_invertida + palavra[i]

    if palavra_invertida == palavra:
        print('É palindromo')
    else:
        print('Não é palindromo')


e_palindromo('diego')
e_palindromo('ana')

#%%
# 3. Análise de Lista Numérica (Nível: Básico/Intermediário)

# Crie uma função chamada analisar_numeros que receba uma lista de números e
# retorne um dicionário contendo três chaves: "maior", "menor" e "media".

# Exemplo de entrada: analisar_numeros([10, 20, 30, 40])

# Saída esperada: {'maior': 40, 'menor': 10, 'media': 25.0}

numeros = [10, 20, 30, 40]

def analisar_numeros(numeros: list):

    numeros_ordenados: list = sorted(numeros)

    dicionario_maior_menor_media: dict = {}

    dicionario_maior_menor_media = {'maior': numeros_ordenados[-1],
                                'menor': numeros_ordenados[0],
                                'media': sum(numeros_ordenados) / 
                                len(numeros_ordenados)}

    return dicionario_maior_menor_media

analisar_numeros(numeros)

#%%
# 4. Validador de Senha Forte (Nível: Intermediário)
# Desenvolva uma função chamada validar_senha que receba uma string e
# verifique se ela atende a todos os critérios abaixo, retornando True ou False:

# Ter no mínimo 8 caracteres.

# Conter pelo menos uma letra maiúscula.

# Conter pelo menos um número.

# Exemplo de entrada: validar_senha("Python123")

# Saída esperada: True

def validar_senha(senha: str) -> bool:
    valida = True

    if len(senha) < 8:
       valida = False

    if not any(caractere.isupper() for caractere in senha):
       valida = False

    if not any(caractere.isdigit() for caractere in senha):
        valida = False
    
    return valida

validar_senha("Python123")
