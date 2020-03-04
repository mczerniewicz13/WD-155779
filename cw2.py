# wejscie=input()
# print(wejscie)
# print(type(wejscie))

# liczba=10

# if liczba <10:
#     print("costam")

# elif liczba >0:
#     print("costam2")

# else:
#     print("klapa")

# if liczba >0 and liczba<11:
#     print("ok")

# #krocej
# if 0<liczba<11:
#     print("ok")

# != różny od

#foreach
# imie="Ariadna"

# for litera in imie:
#     print(litera)

range(5) #start,stop,step. Tylko stop jest wymagany i jedna wartosc to zawwszze stop
#stop = stop - step czyli bierze przedostatni element
# print(range(5))
# print(type(range(5)))
# print(list(range(2,10,2)))
# print(list(range(10,2,-2)))
# print(list(range(0,-10,-2)))

#od do 
# tutaj stop tez dziala o jeden w tył
#nie podajac wartosci domyslnie ustawia poczatek:koniec:1
# print(imie[::2])



# for liczba in range(5):
#     pass

# for litera in imie[::2]:
#     pass

# def funkcja():
#     pass

# #zad1
# zdanie = input("Podaj zdanie\n")
# wynik=0
# for litera in zdanie:
    
#     if litera == " ":
#         wynik+=1

# print(wynik)

# #zad2
# import sys
# print("Podaj pierwsza liczbe")
# a = sys.stdin.readline()
# print("Podaj druga liczbe")
# b = sys.stdin.readline()
# c=int(a)*int(b)
# sys.stdout.write(str(c))

# #zad3
# #zad4
# bezw=input("\nPodaj liczbe")
# print(abs(int(bezw)))

# #zad5
# a=input("Podaj a\n")
# b=input("Podaj b\n")
# c=input("Podaj c\n")
# if 0<int(a)<=10 and int(a)>int(b) or int(b)>int(c):
#     print("Liczby spelniaja warunek")
# else:
#     print("Liczby nie spelniaja warunku")

# #zad6
# for x in range(0,501,5):
#     print(str(x)+", ")

# #zad 7
# while 1>0:
#     a=input("Podaj liczbe\n")
#     if a == "x":
#         break
#     else:
#         print(pow(int(a),2))

# #zad8
# lista = []
# while True:
#     a=input("Podaj liczbe\n")
#     if a == "x":
#         break
#     else:
#         lista.append(int(a))
# print(lista)

# #zad9
# a=input("Podaj liczbe\n")
# b=[]
# wynik=0
# i=0
# while len(a)!=len(b):
#     b.append(a)
#     wynik+=int(a[i])
#     i+=1
# print(wynik)

# #zad10
# a=input("Podaj wysokosc <10\n")
# for i in range(int(a)):
#     for j in range(i+1):
#         print("A", end='') #end sprawia ze nie stawia sie na koncu automatycznie nowa linia tylko pusty znak
#     print("\n")

#zad11
symbol="o"
a=input("Podaj wielksoc od 3 do 9 nieparzyste\n")
# x=int(a)
# for i in range(1,x,2):
#     print(f"{symbol*i:^x}")
for i in range