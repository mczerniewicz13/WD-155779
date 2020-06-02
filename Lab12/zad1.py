from lxml import html
import requests

url = "https://boardgamegeek.com/"
data = requests.get(url)
page = html.fromstring(data.text)
xpath = '//div[@id="results_1"]//h2[@class="media-cell__title"]//a[@ng-href]'
foundElements = page.xpath(xpath)
for element in foundElements :
    print('https://boardgamegeek.com'+element.items()[2][1])
