import numpy as np 
import pandas as pd 
import xlrd
import openpyxl
import matplotlib.pyplot as plt
xlsx = pd.ExcelFile('imiona.xlsx')
narodziny = pd.read_excel(xlsx,'Arkusz1')

latak=(narodziny.groupby(['Plec','Rok']).agg(sum).loc['K'])['Liczba']
latam=(narodziny.groupby(['Plec','Rok']).agg(sum).loc['M'])['Liczba']

plt.bar(latak.index.values,latak.values, label='Kobiety')
plt.bar(latam.index.values,latam.values, label='Mezczyzni', bottom = latak.values)
plt.legend()


plt.show()