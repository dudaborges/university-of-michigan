import requests
from bs4 import BeautifulSoup

url = "https://g1.globo.com/mundo/noticia/2023/05/04/charles-iii-indigenas-de-ex-colonias-britanicas-querem-pedido-de-desculpas-por-legado-de-genocidio.ghtml"
response = requests.get(url)
htmlUrl = response.content
soup = BeautifulSoup(htmlUrl, 'html.parser')
text = soup.get_text()
with open("./dictionaries/web.txt", "w", encoding="utf-8") as file:
    file.write(text.lower())
