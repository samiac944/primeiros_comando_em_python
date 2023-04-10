"""
#FOR 
Permite fazer repetição controlada, dentro de uma range(faixa).

for --> para

range --> faixa, parametro.

variavel --> qualquer nome de variável.
"""

#EXEMPLO 1 (com 1 parâmetro)

for variavel in range(10):
    print(variavel)

#faixa menor que 5, possui somente 1 parâmetro.



#EXEMPLO 2 (com 2 parâmetro)

for i in range(1, 10):
    print(i)

#faixa que começa no 1 e termina em menor que 10.


#EXEMPLO 3 (com 3 parâmetro, o terceiro paramentro significa quanto queremos pular.)

for i in range(0, 20, 2):
    print(i)

# EXEMPLO 4 (automatizar solicitação com for)
# f --> quando colocado antes da string, você consegue adicionar uma variavel.
# {} --> para adicionar uma variavel.
# sempre colocar : no final.

soma = 0

for i in range(1, 4):
    nota = float(input(f'insira sua nota {i} '))

    soma = soma + nota

print(soma / 3)