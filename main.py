from allUrls import allUrls
import requests
from bs4 import BeautifulSoup
import re

def main():
    print('Starting execution\n')

    url = 'http://itaudeminas.mg.gov.br/'

    result = requests.get(url)
    links = []

    soup = BeautifulSoup(result.content, 'html.parser')

    file = open('links.txt', 'a')

    for link in soup.find_all('a'):
        if type(link.get('href')) == str and re.match('^http', link.get('href')):
            links.append(link.get('href'))
    
    newLinks = list(dict.fromkeys(links))
   
    for link in newLinks:
        if type(link) == type('a'):
            file.write(link)
            file.write('\n')

    allUrls(links, file)
    
if __name__ == "__main__":
    main()