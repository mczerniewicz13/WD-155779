def same(tekst):
    usuniete = 0
    nowe=""
    for litera in tekst:
        if litera !="a" and litera !="e" and litera !="i" and litera !="o" and litera !="u" and litera !="y":
            nowe += litera
        else:
            usuniete+=1
    print(nowe)
    print("Usuniete: "+ str(usuniete))

same("Albert")



