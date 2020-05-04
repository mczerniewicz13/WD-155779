
import pandas as pd 
zam = pd.read_csv('zamowienia.csv', header=0, delimiter=';')
#Kraj;Sprzedawca;Data zamowienia;idZamowienia;Utarg

#3a=========================
# unik=zam['Sprzedawca'].unique()
# print(unik)

#3b=========================
# maks=zam.sort_values('Utarg', ascending = False).iloc[[0,1,2,3,4]]
# print(maks['Utarg'])

#3c=========================
# ile=zam.groupby(['Sprzedawca']).count()
# print(ile['idZamowienia'])

#3d=========================
# suma=zam.groupby(['Kraj']).count()
# print(suma['idZamowienia'])

#3e=========================
# rok = zam[(zam['Data zamowienia'] >= '2005-01-01') & (zam['Data zamowienia'] <= '2005-12-31') & (zam['Kraj']=='Polska')].groupby(['Kraj']).count()
# print(rok['idZamowienia'])

#3f=========================
# sre = zam[(zam['Data zamowienia'] >= '2004-01-01') & (zam['Data zamowienia'] <= '2004-12-31')].mean()
# print(sre['Utarg'])

#3g=========================
# cztery = zam[(zam['Data zamowienia'] >= '2004-01-01') & (zam['Data zamowienia'] <= '2004-12-31')]
# piec = zam[(zam['Data zamowienia'] >= '2005-01-01') & (zam['Data zamowienia'] <= '2005-12-31')]
# cztery.to_csv('zamowienia_2004.csv', header=None)
# piec.to_csv('zamowienia_2005.csv', header=None)