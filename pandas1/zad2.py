import numpy as np 
import pandas as pd 
import xlrd
import openpyxl
xlsx = pd.ExcelFile('imiona.xlsx')
narodziny = pd.read_excel(xlsx,'Arkusz1')

#2a=========================
# print(narodziny[narodziny['Liczba']>1000])

#2b=========================
# print(narodziny[narodziny['Imie']=='MATEUSZ'])

#2c=========================
# print((narodziny.groupby(['Rok']).agg({'Liczba':['sum']})).sum())

#2d=========================
# piec=narodziny[((narodziny.Rok >=2000) & (narodziny.Rok<=2005))]
# print(piec.groupby(['Rok']).agg({'Liczba':['sum']}))

#2e=========================
# print(narodziny.groupby(['Plec']).agg({'Liczba':['sum']}))

#2f=========================
# imie = narodziny.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0)
# print(imie)

#2g=========================
# pop=narodziny.groupby(['Plec','Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'), ascending = False).iloc[[0,1]]
# print(pop)


