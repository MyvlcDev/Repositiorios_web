import requests
from bs4 import BeautifulSoup

def buscar_noticias_molina():
    # URL de búsqueda en infomolina.es
    url = "https://infomolina.es/molina"
    # Realizar la solicitud HTTP
    response = requests.get(url)
    # Analizar el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser') 
    # Encontrar todos los elementos <a> (enlaces) en la página
    links = soup.find_all('a')
    count = 0 
    max_news= 5

    print("\nNoticias de ultima hora relacionadas con Molina de Segura.\n")
    
    # Encontrar todos los elementos <a> (enlaces) en la página
    h2_tag = soup.find_all('h2')
    for h2 in h2_tag:
        # Encuentra todos los enlaces dentro de la etiqueta h2
        links = h2.find_all('a')
        # Imprime el texto de cada enlace
        for link in links:
            print(link.get_text())   
            count += 1
        if count >= max_news:
            break
        if count >= max_news:
            break 


if __name__ == "__main__":
    buscar_noticias_molina() 


