'''numero = int(input('Insira um número: '))
print(numero)

if numero < 0:
    print('Número negativo')

elif numero % 2 == 0:
    print('Número par')'''

cont = 0
resultado = 0
n = 1000

while cont != n:

    resultado = resultado + 1/(2**cont)

    cont = cont + 1

print(resultado)
