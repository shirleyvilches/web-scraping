import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2024/07/por-que-se-utiliza-python-en-ciencia-de.html')
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# Extraer titulo
print(sopa.select('title')[0].getText())

# Extraer elemento de una clase
columna_lateral = sopa.select('h3.post-title')
print(columna_lateral[2].getText())

# Extraer imagen
img_element = sopa.select('img')
img = img_element[1]['src']

"""
Este bloque extrae la imagen y la guarda

img_save = requests.get(img)
f = open("mi imagen.jpg", 'wb')
f.write(img_save.content)
f.close()

"""

