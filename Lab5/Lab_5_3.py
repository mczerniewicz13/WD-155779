class Kwadrat():

    def __init__(self, x):
        self.x = x
    
    def __ge__(self,kwadrat):
        if self.x >= kwadrat.x:
            return True
        else:
            return False

    def __gt__(self,kwadrat):
        if self.x > kwadrat.x:
            return True
        else:
            return False

    def __le__(self,kwadrat):
        if self.x <= kwadrat.x:
            return True
        else:
            return False

    def __lt__(self,kwadrat):
        if self.x < kwadrat.x:
            return True
        else:
            return False


kw1 = Kwadrat(3)
kw2 = Kwadrat(5)

if kw1 >= kw2 :
    print("kw1 >= kw2")
if kw1 > kw2 :
    print("kw1 > kw2")
if kw1 < kw2 :
    print("kw1 < kw2")
if kw1 <= kw2 :
    print("kw1 <= kw2")





