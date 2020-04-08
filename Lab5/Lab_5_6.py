class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

lista = Wspak([1,2,3,4,5])
napis = Wspak("Kredens pod zegarem")
#liczba = Wspak(56849) nope
print(next(lista))
print(next(napis))
print(next(lista))
print(next(napis))
print(next(lista))
print(next(napis))
print(next(lista))
print(next(napis))
