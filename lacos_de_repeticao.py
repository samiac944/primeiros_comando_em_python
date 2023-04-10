# WHILE = enquanto. Looping infinito. Repetição não controlada.


numero_secreto = 15
numero_digitado = int(input("Digite um número de 1 a 20... "))

# != --> diferente
#while --> enquanto
# : --> então
while numero_secreto != numero_digitado:
    print("Você errou, tente novamente")

    numero_digitado = int(input("Digite um número de 1 a 20... "))

print("Parabéns, você acertou!")

# EXEMPLO 2 --> repetição controlada

contador = 0

while contador < 5:
    print(contador)

    contador = contador + 1


