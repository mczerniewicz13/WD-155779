def licze(tekst):
    ile=0
    for litera in tekst:
        if litera != " " and litera != "," and litera != ".":
            ile+=1
    return ile

print(licze("A l,a."))