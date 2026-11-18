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

# Saída esperada: True

def e_palindromo(palavra: str):
    palavra_invertida = ''
    for i in range(len(palavra)-1, -1, -1):
        palavra_invertida = palavra_invertida + palavra[i]

    if palavra_invertida == palavra:
        print('É palindromo')
    else:
        print('Não é palindromo')

e_palindromo('diego')
e_palindromo('ana')

