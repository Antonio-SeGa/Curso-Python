import bs4
import requests

# Crear URL sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# Iterar paginas
for pagina in range(1, 51):
    
    # Crear sopa en cada pagina 
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:

        # Chequear que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # Guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            # Agregar librp
            titulos_rating_alto.append(titulo_libro)


# Ver los libros de 4 o 5 estrellas 
for t in titulos_rating_alto:
    print(t)

