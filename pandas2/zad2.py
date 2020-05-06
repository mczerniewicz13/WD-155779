import pandas as pd 
import matplotlib.pyplot as plt
import xlrd
import openpyxl
xlsx = pd.ExcelFile('imiona.xlsx')
imiona = pd.read_excel(xlsx,'Arkusz1')
plec=imiona.groupby(['Plec']).count()
plec=plec['Imie']
wykres=plec.plot.bar()
wykres.set_ylabel('Liczba urodzin')
wykres.set_xlabel('Płeć')
plt.title('Liczba urodzin z podziałem na płeć')
plt.show()