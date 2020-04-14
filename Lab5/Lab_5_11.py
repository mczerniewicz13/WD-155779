def gen():
    x = 0
    y = 1
    for i in range(100):
        z = x + y
        yield z
        x = y
        y = z

f = gen()
for i in range(50):
    print(next(f))

