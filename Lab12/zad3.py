from lxml import html
import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://boardgamegeek.com/browse/boardgame"
data = requests.get(url)

page = html.fromstring(data.text)

xpath = '//*[@id="collection"]//*[@class="table-responsive"]'
table_div = page.get_element_by_id('collection')
table = table_div.xpath('./*[@class="table-responsive"]/table')[0]

headers = [label for label in table.xpath('.//th')]
labels = []

for header in headers:
    anchor = header.xpath('./a/text()')
    if len(anchor) > 0:
        labels.append(anchor[0].strip())
    else:
        labels.append(header.text.strip())



rowy_div = page.get_element_by_id('collection')
rowy = rowy_div.xpath('./*[@class="table-responsive"]/table')[0]

elementy=[element for element in rowy.xpath('.//td')]
linijka=[]

for els in elementy:
    a = els.xpath('./a/text()')
    if len(a) > 0:
        linijka.append(a[0].strip())
    else:
        linijka.append(els.text.strip())

def podzial(lista,n):
    for i in range(0, len(lista), n):
        yield lista[i:i + n]


df=pd.DataFrame(list(podzial(linijka,7)), columns=labels)
df=df.drop(columns=['','Shop'])
df=df.sort_values(['Num Voters'],ignore_index=True)
df=df[0:10]
voters=df['Num Voters']
ix=voters.index.tolist()
val=voters.tolist()


plt.bar(ix, val)
plt.ylabel('Index')
plt.xlabel('Num Voters')
plt.show()
