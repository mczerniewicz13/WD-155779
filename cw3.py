
# imie = 'Marianna'
# lista = []
# for litera in imie:
#     lista.append(litera.upper())

# #równoważnie

# lista = [litera.upper() for litera in imie]
# # lista=[print(litera.upper()) for litera in imie] funkcja print nie zwraca wartości
# print(lista)

# #suma cyfr
# liczba = 123456789
# print(sum([int(cyfra) for cyfra in str(liczba)]))


# #pierwsze 5 poteg liczby 2
# print([2**n for n in range(5)])


# #parzyste elementy listy
# lista=[
#     [1, 2],
#     [3, 4]]
# print([element for wiersz in lista for element in wiersz if element %2 == 0])
# #równoważnie
# wynik=[]
# for wiersz in lista:
#     for element in wiersz:
#         if element %2 == 0:
#             wynik.append(element)


# imie = 'Marianna'
# #(index,wartosc) <--- krotka, para wartosci, enumerate zwraca krotke
# #{0:'M',...}
# #{para[0]:para[1] for para in enumerate(imie)}
# slownik = {klucz:wartosc for klucz,wartosc in enumerate(imie)}
# slownik_odwr = {wartosc:klucz for klucz,wartosc in enumerate(imie)}
# print(slownik)
# print(slownik_odwr)



# #set - zbiory
# litery = set(imie)
# print(litery)


# #krotki
# #rozpakowanie krotki
# imie,nazwisko = ('Marian','Bąbel')


# #rozpakowanie kolekcji
# print({*range(9)})

# from timeit import timeit #mierzy czas wykonania czegos

# print(timeit("{*range(9)}", number=100000))
# print(timeit("set(range(9))", number=100000))



# kod = """
# lista=[
#     [1, 2],
#     [3, 4]]
# wynik=[]
# for wiersz in lista:
#     for element in wiersz:
#         if element %2 == 0:
#             wynik.append(element)"""
# kod2 = """lista=[
#     [1, 2],
#     [3, 4]]
# [element for wiersz in lista for element in wiersz if element %2 == 0]"""
# print(timeit(stmt=kod, number=100000))
# print(timeit(stmt=kod2, number=100000))




# #funckje
# def dodaj(liczba1,liczba2):
#     return liczba1 + liczba2

# dodaj(2, 3)

# def witaj(imie='Jan'):
#     print(f'Witaj {imie}!')
# witaj()
# witaj('Arkadiusz')

# #def witaj(imie, nazwisko='Kowalski') OK
# #def witaj(imie = 'Jan', nazwisko) NIE OK bo najpierw te ktore dajemy a potem te z wartosciami domyslnymi

# #funkcja z gwiazdka uzywana jest gdy nie znami liczby argumentow
# #def suma(*liczby):




# #moduły i pakiety

# # import start #plik z mojego folderu
# # start.pow() #fucnkja w tym pliku


# #zad 11 z listy 2
# def diamond(width=11, symbol="o"):
#     for level in range(1,width+2,2):
#         print(f'{symbol*level:^{width}}')
#     for level in range(width-2,0,-2):
#         print(f'{symbol*level:^{width}}')
# diamond()




# #slicing
# imie = "Małgorzata"
# print(imie[0])
# print(imie[-1]) #ostatni element dzieki temu nie musimy wiedziec jak dlugi jest ciag)
# print(imie[-3:]) # od 3 od konca do ostatniego [od:do]

# print(imie[:2])

# #range(start, stop, step)
# print(imie[::2]) #co druga litera
# print(imie[::-2])


#zad1
A = [1/x for x in range(1,11)]
print(A)
B = [2**n for n in range(11)]
print(B)
C = [x for x in B if x %4 == 0]
print(C)


#zad2
#-------

#zad3
zakupy = {'jajka':'opak', 'mleko':'l', 'ser':'kg', 'jablka':'kg', 'spodnie':'szt', 'bulki':'szt'}
lista = {klucz:wartosc for klucz,wartosc in zakupy.items() if wartosc == 'szt'}
print(lista)

#zad4
def monotonicznosc(a):
    
    if int(a)>0:
        print("Funkcja rosnaca")
    elif int(a)<0:
        print("Funkcja malejaca")
    elif int(a)==0:
        print("Funkcja stala")
    else:
        print("Ty głuptasie a nie jest liczbą")

monotonicznosc(2)


