# LISTAS

#[] --> Referente à listas
# permite diferentes tipos de dados.

# com listas
notas = [7, 8.5, 10]

# tipos de listas

# vazia
listas = []

#vazia
listas = list()

# com diferentes tipos de dados
listas = [9, 'nome', True]

# permite criar lista dentro de outra lista
listas =[9, 10, [1, 2]]


# INDEXAÇÃO 
#acessar elemento da lista atraves do indice
# indexar com valores negativos, acessa a partir do ultimo indice

lista = ['Sâmia', 'Maria Tereza', 'Luiz']

print(lista[0])
print(lista[1])
print(lista[2])


# SLICES (Fatiamento)
# Permite acessar os indices por faixa
# Quando coloca os : acessa até a faixa solicitada

lista = [10, 20, 30, 40, 50]

print(lista[0:3])

#pega a partir do indice solicitado até o final da lista

print(lista[3:])

#o ultimo parametro define quantos deve pular

print(lista[0:5:2])

#PERCORRER LISTA UTILIZANDO for

for elemento in lista:
    print(elemento)

#UTILIZANDO len PARA SABER QUANTOS ELEMENTOS EXISTEM NA LISTA 

print(len(lista))

for i in range(len(lista)):
    print(i)
