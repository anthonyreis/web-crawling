from allUrls import allUrls
import requests
from bs4 import BeautifulSoup

def main():
    print('Starting execution\n')

    url = 'http://itaudeminas.mg.gov.br/'

    result = requests.get(url)
    links = []

    soup = BeautifulSoup(result.content, 'html.parser')

    file = open('links.txt', 'a')

    for link in soup.find_all('a'):
        links.append(link.get('href'))
        
    for link in links:
        if type(link) == type('a'):
            file.write(link)
            file.write('\n')

    allUrls(links, file)
    
if __name__ == "__main__":
    main()