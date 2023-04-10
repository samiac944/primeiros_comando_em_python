# ESTRUTURAS CONDICIONAIS

"""
if = se
else = do contrário
elif = do contrário se
elif é utilizado quando queremos realizar a verificação de outra 
expressão caso a primeira2 validação seja falsa.
: = então
"""

idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# EXERCÍCIO MÉDIA 

media = float(input("Qual a sua nota? "))

if media >= 7:
    print("Você está aprovado!")
elif media >= 5:
    print("Você está em recuperação!")
else:
    print("Você está reprovado!")