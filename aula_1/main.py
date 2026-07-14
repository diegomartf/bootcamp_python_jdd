# desafio

nome = input('Digite seu nome: ')
salario = input('Digite o valor do seu salario: ')
pctBonus = int(input('Digite sua porcentagem de bonus: '))

try:
    valor_do_bonus = 1000 + salario * pctBonus
    print(f'O seu bonus esse mês é {valor_do_bonus} reais')
except TypeError:
    print('O salario e o percentual precisam ser apenas numeros')
    print('Tente novamente')
