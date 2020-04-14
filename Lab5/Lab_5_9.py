    
def gen(data):
    for index in range(len(data)):
        if index % 2 == 0:
            yield data[index]
        

napis = gen("Tomek")
print(next(napis))
print(next(napis))
print("Alabama")
print(next(napis))


