import pandas as pd 
import matplotlib.pyplot as plt

zam = pd.read_csv('zamowienia.csv', header=0, delimiter=';')
ile=zam.groupby(['Sprzedawca']).count()
ile=ile['idZamowienia']
wykres=ile.plot.bar()
plt.show()