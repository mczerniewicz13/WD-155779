import pandas as pd 
import matplotlib.pyplot as plt

zam = pd.read_csv('zamowienia.csv', header=0, delimiter=';')
ile=zam.groupby(['Sprzedawca']).count()['idZamowienia']
sprzedawcy=ile.index.values
plt.pie(ile, labels=sprzedawcy, autopct = lambda pct: "{:.1f}%".format(pct), shadow = True)
plt.legend(title='sprzedawcy', loc = 4, framealpha=0.5)
plt.show()