class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstuktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(5,5)
p1.update(3)
print(p1.counter)
print(p2.counter)
p1.update(1)
p2.update(2)
p3 = Point(1,1)
print(p3.counter)