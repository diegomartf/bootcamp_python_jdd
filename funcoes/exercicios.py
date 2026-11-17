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

palavra = 'diego'

palavra_invertida = reversed(palavra)

print(palavra_invertida)
