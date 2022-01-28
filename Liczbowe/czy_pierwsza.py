# Ten plik jest częścią repozytorium "Algorytmy Maturalne 2023" należącego do https://github.com/CuPidev
# Zachęcam do dołączenia do discorda o tematach informatycznych -> https://discord.gg/pQQW9hX
# Jeśli chcesz wesprzeć autora to możesz zostawić:
# followka na twitterze:
# subika na youtube:
# napiwek:

"""Funkcja sprawdza czy podana liczba jest liczbą pierwszą, metodą prostą."""

from math import sqrt


def czy_pierwsza(liczba: int) -> bool:
    for i in range(2, sqrt(liczba)):
        if liczba % i == 0:
            return False
    return True
