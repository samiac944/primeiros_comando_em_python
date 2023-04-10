# METODOS E FUNÇÕES DE LISTAS

lista = [1, 2, 3, 4]
print('Sem alteração', lista)

# 1. APPEND
# adicionar um item no final da lista.          

lista.append(5)
print(lista)

# 2. INSERT
# escolhe onde e qual alimento que quer adicionar.)
# o primeiro parametro é o indice e o segundo parametro é o objeto.

lista.insert(0, 0)
print(lista)

# 3. EXTEND
# adiciona uma lista no final de outra lista.

lista2 = [6, 7, 8]
lista.extend(lista2)

print(lista)

# 4. POP
# remove um elemento especificado, se não indicar o elemento
# a ser eliminado, o pop elimina o ultimo elemento.

# sem expecificar, elimina o ultimo
lista.pop()
print(lista)

# especificando, remove o indice especificado.
lista.pop(0)
print(lista)

# 5. REMOVE
# remove o item especificado, sempre remove o primeiro que encontrar.
lista.remove(5)
print(lista)

# 6. COUNT
# Conta a quantidade de um determinado elemento.
print(lista.count(6))

# 7. INDEX 
# Diz qual o indice de determinado elemento.
print(lista.index(3))

# 8. SORT
# Ordenar e organiza a lista de forma crescente.
lista.sort()
print(lista)

# Ordenar e organiza a lista de forma decrescente.
lista.sort(reverse=True)
print(lista)

