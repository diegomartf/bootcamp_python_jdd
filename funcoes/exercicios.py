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
