import numpy as np 
import pandas as pd 
import xlrd
import openpyxl
import matplotlib.pyplot as plt
xlsx = pd.ExcelFile('imiona.xlsx')
narodziny = pd.read_excel(xlsx,'Arkusz1')
plec=narodziny.groupby(['Plec']).agg(sum)['Liczba']
etykiety=['K','M']
wartosci=[plec[0],plec[1]]
plt.subplot(1,3,1)
plt.bar(etykiety,wartosci)

latak=(narodziny.groupby(['Plec','Rok']).agg(sum).loc['K'])['Liczba']
latam=(narodziny.groupby(['Plec','Rok']).agg(sum).loc['M'])['Liczba']
plt.subplot(1,3,2)
plt.plot(latak.index.values,latak.values, label='Kobiety')
plt.plot(latam.index.values,latam.values, label='Mezczyzni')
plt.legend()

suma=narodziny.groupby(['Rok']).agg(sum)['Liczba']
x=suma.index.values
y=suma.values
plt.subplot(1,3,3)
plt.bar(x,y)
plt.show()