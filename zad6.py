def polacz_listy(lista_1: list, lista_2: list) -> list:
    lista_polaczona = lista_1 + lista_2
    lista_bez_duplikatow_i_potega = []
    for element in lista_polaczona:
        if element not in lista_bez_duplikatow_i_potega:
            lista_bez_duplikatow_i_potega.append(element)

    lista_bez_duplikatow_i_potega = [x ** 3 for x in lista_bez_duplikatow_i_potega]

    return lista_bez_duplikatow_i_potega

lista_1 = [2,4,6,8]
lista_2 = [1,2,3,4]

wynik = polacz_listy(lista_1, lista_2)
print(wynik)