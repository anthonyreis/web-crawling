import requests
from bs4 import BeautifulSoup
import re
from removeDuplicate import removeDuplicate

def allUrls(allLinks, file):
    try:
        print('Gathering URLs\n')
        for url in allLinks:
            if type(url) == str and re.match('^http', url):
                result = requests.get(url)
                soup = BeautifulSoup(result.content, 'html.parser')
                
                for link in soup.find_all('a'):
                    newLink = link.get('href')
                    if type(newLink) == str:
                        if re.match('^http', newLink) and newLink not in allLinks:
                            allLinks.append(newLink)
                            file.write(newLink)
                            file.write('\n')
                        elif re.match('^/', newLink):
                            auxLink = url + newLink
                            if auxLink not in allLinks:
                                allLinks.append(auxLink)
                                file.write(auxLink)
                                file.write('\n')
                            else:
                                print(f'URL repetido: {auxLink}')
                        elif re.match('^http', newLink):
                            print(f'URL repetido: {newLink}')
                        
        file.flush()
        file.close()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(f'Exception Ocurred, {message}\n')
    finally:
        print('All done :) \n')
    
    