# FUNÇÕES
 
#um trecho de código que possui 
# uma responsabilidade específica e que damos um nome à ele.

"""
print() imprime uma mensagem na tela
input() digitar dados
len() qtd de elementos na lista
max() retorna o maior elemento na lista
"""

# CRIANDO FUNÇÃO

# função inicial

"""def --> DEFININDO UMA FUNÇÃO"""
def saudacao():
    print('Seja bem-vindo(a)!')
    print('É uma prazer ter você fazendo parte desse curso!')

saudacao()

# FUNCAO COM PARAMETRO
""" Parametro deve ser adicionado dentro do parenteses, 
depois do nome da funcao """

def parametro(nome):
    print(f'Olá, {nome}')
    #f --> quando colocado antes da string, você consegue 
    # adicionar uma variavel.
    # {} --> para adicionar uma variavel
    print('Sempre o parâmetro fica dentro do parenteses.')

parametro('Sâmia')


