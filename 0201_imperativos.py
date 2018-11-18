import requests
from lxml import html

def download(url):
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("! Error {} retrieving url {}".format(r.status_code, url))
    return r

lista_imperativos = []
xpath_string = '//html/body/div[3]/div[3]/div[4]/div[2]/div/div/div/div/ul/li/a/@title'
url = '/w/index.php?title=Categor%C3%ADa:ES:Imperativos&from=A'

while url != None:
    page = download('https://es.wiktionary.org' + url)
    # Necesito cargar mi html en una estructura de árbol XML
    tree = html.fromstring(page.content)
    urls = tree.xpath('/html/body/div[3]/div[3]/div[4]/div[2]/div/a[4]/@href')
    if len(urls) > 0:
        url = urls[0]
    else:
        url = None
    # Hago la llamada al XPath para obtener los resultados
    results = tree.xpath(xpath_string)
    for result in results:
        lista_imperativos.append(result)

archivo_imperativos = open("0202_lista_imperativos.txt","w")
for imperativo in lista_imperativos:
    archivo_imperativos.write(imperativo + '\n')
archivo_imperativos.close()

