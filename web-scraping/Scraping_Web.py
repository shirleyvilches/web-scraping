import bs4
import requests

# Llaves para poder usar loop para cambiar de paginas
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Lista rating alto
lista_rating_alto = []

# Iterar en todas las paginas
for pag in range(1, 51):
    # crear sopa de cada pagina
    url_pag = url_base.format(pag)
    resultado = requests.get(url_pag)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')
    for libro in libros:
        #checkear si tiene 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            #guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']
            #agregar libro a lista
            lista_rating_alto.append(titulo_libro)

# Ver los libros de 4 o 5 estrellas en consola
for t in lista_rating_alto:
    print(t)

