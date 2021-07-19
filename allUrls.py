import requests
from bs4 import BeautifulSoup
import re
from removeDuplicate import removeDuplicate

def allUrls(allLinks, file):
    try:
        print('Gathering URLs\n')
        for url in allLinks:
            print(f'url: {url}')
            if type(url) == str and re.match('^http', url):
                result = requests.get(url)
                soup = BeautifulSoup(result.content, 'html.parser')
                
                for link in soup.find_all('a'):
                    if type(link.get('href')) == str and re.match('^http', link.get('href')):
                        file.write(link.get('href'))
                        file.write('\n')
        file.flush()
        file.close()
        removeDuplicate('links.txt')
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(f'Exception Ocurred, {message}\n')
        removeDuplicate('links.txt')
    finally:
        print('All done :) \n')
    
    