import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import xlrd
import openpyxl
xlsx = pd.ExcelFile('imiona.xlsx')
imiona = pd.read_excel(xlsx,'Arkusz1')
roki=imiona.groupby(['Rok']).count()
roki=roki['Imie']
wykres=roki.plot.bar()
wykres.set_ylabel('Liczba urodzin')
wykres.set_xlabel('Rok')
plt.title('Liczba urodzin z podziałem na lata')
plt.show()