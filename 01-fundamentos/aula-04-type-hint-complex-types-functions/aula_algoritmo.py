# Implementação do algoritmo de ordenação por seleção
lista_n: list = [40,50,60,70,0,-408593,1,50]
lista_n_02: list = [40,60,70,0,-408593,1,50]
lista_n_03: list = [40,60,70,0,1,50]

def ordenar_lista_de_numeros(numeros: list) -> list:
    nova_lista_de_numeros = numeros.copy()

    for i in range(len(nova_lista_de_numeros)):
        for j in range(i+1, len(nova_lista_de_numeros)):
            if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
                nova_lista_de_numeros[i], nova_lista_de_numeros[j] = nova_lista_de_numeros[j], nova_lista_de_numeros[i]
   
    return nova_lista_de_numeros

# Ordenando a lista
nova_lista = ordenar_lista_de_numeros(lista_n)
nova_lista_2 = ordenar_lista_de_numeros(lista_n_02)
nova_lista_3 = ordenar_lista_de_numeros(lista_n_03)


