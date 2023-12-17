def czy_jest_wartosc(lista: list, wartosc: int) -> bool:
    if wartosc in lista:
        return True
    else:
        return False

moja_lista = [1, 2, 3, 4, 5, 6, 7]
moja_liczba = 10

wynik = czy_jest_wartosc(moja_lista, moja_liczba)
print(wynik)
