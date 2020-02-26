# print("Hello world!")

# # for element in kolekcja:
# #     for element2 in kolekcja2: ctrl + /

# def funkcja():
#     print("Ala")
#     a=5
#     imie = "Zbyszek"

# a = 5
# print(type(a))

# imie = "Ala"
# imie = 'Ala'
# # alt+shift+strzalka w dol/gore

# imie = """Ala
# ma kota
# Filemona"""
# # """ """ pozwala na format tekstu
# print(type(imie))
# imie = 6
# print(type(imie))
# imie = 6.3
# print(type(imie))

# # def funkcje():
# #     """ docstring """
# #     pass

# liczba = str(5)
# liczba = int("5")
# liczba = int("5.5")

imie = "ala"
imie = imie.capitalize()
print(imie)

print(imie[0])

print("ala".capitalize().count("A"))

print(imie + imie)



#formatowanie wyjścia

print(imie + " ma " + str(5) + " lat")

print("{} ma {} lat".format(imie,5))
print("{0} ma {1} lat".format(imie,5))

wiek = 5
print(f"{imie} ma {wiek} lat")

#listy

lista = []
lista = [1, 4, "Ala", 4.5, imie,[1, 2]]

lista[0]
lista[5][1] #2

lista.append(3)

lista[0] = 10

lista2= lista + lista

lista_nowa = list()

# słownik

slownik = {}
slownik = {"imie":"Marek","wiek":35} #klucz:wartosc

slownik["imie"] #odwolanie

print(slownik.keys())
print(slownik.values())
print(slownik.items())

from math import * # importuje wszystko ale moze nadpisac metody ktore nazywaja sie tak samo w naszym protgramie i w przestrzeni math
import math as m # nadaje alias metodom z math
from math import pow as m_pow # importuje tylko wskazana metode pow