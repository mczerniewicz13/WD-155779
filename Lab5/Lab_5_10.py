import itertools
liczby = {1,2,3,4,5,6,7,8,9,10}
wyniki=itertools.combinations(liczby,3)
print(next(wyniki))
print(next(wyniki))
print(next(wyniki))