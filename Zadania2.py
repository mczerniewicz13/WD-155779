# #zad12
# for i in range(1,11,1):
#     for j in range(1,11,1):
#         print(i,"x",j,"=",i*j)
#     print("\n")

# #zad14
# import math
# x=input("Podaj liczbe\n")
# try:
#     print(math.sqrt(int(x)))
# except ValueError:
#     print("No co ty głuptasku, liczba musi być większa lub równa 0")

#zad15
x=input("Podaj liczbe\n")
try:
    a=x+5
except TypeError:
    print("Przecież widzę, że to nie liczba")


