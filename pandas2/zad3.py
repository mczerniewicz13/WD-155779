import pandas as pd 
import matplotlib.pyplot as plt
import xlrd
import openpyxl
xlsx = pd.ExcelFile('imiona.xlsx')
imiona = pd.read_excel(xlsx,'Arkusz1')
plec=imiona[(imiona['Rok']>=2012)].groupby(['Plec']).count()
plec=plec['Liczba']
wykres = plec.plot.pie(subplots=True, autopct='%.2f%%', fontsize=15)
plt.title('Ilosc urodzonych dzieci z podziałem na płeć')
plt.show()
