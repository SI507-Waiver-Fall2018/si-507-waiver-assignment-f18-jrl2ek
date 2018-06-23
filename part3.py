# these should be the only imports you need

import requests
from requests import get
from bs4 import BeautifulSoup
from bs4 import NavigableString

#Name: John Robert Lint
#Umich uniqname: jrlint

def accessLink(link):
    loc = link[:5]
    if loc == '/sect':
        page = 'https://www.michigandaily.com' + link
        site = requests.get(page)

        content = site.content
        soup = BeautifulSoup(content, 'html.parser')
        results = soup.find('div', attrs={'class': 'link'})
        results.find_all('a')
        x = 1

        for result in results:
            if isinstance(result, NavigableString):
                continue
            else:
                print("  by ", sep='', end='')
                print(result.text)


        """for result in results:
            print(x)
            print(link)
            print('This is the result', result.text)
            x+=1"""
    elif loc == '/news':
        page = 'https://www.michigandaily.com' + link
        site = requests.get(page)

        content = site.content
        soup = BeautifulSoup(content, 'html.parser')
        results = soup.find('p', attrs={'class': 'info'})
        #print(results)
        #print("results[0] ", results[0])
        for result in results:
            print("  by ", sep='', end='')
            print(result)
            break

def main():
    page = 'https://www.michigandaily.com/'

    site = requests.get(page)

    content = site.content
    soup = BeautifulSoup(content, 'html.parser')

    results = soup.find('div', attrs={'class': 'panel-pane pane-mostread'})
    results = results.find_all('a')
    #link_list = [a['href'] for a in results.find_all('a', href=True)]
    #print(type(results))
    x=1
    titles = []
    links = []
    for result in results:
        #if result.div:
            #print(result.div)
            #print('hi')
       # print(result)
        titles.append(result.text)
        #print(result.text)
        links.append(result['href'])
        #print(result['href'])
        x+=1

    print('Michigan Daily -- MOST READ')
    #print(titles)
    #print(links)
    x = 0
    for link in links:
        print(titles[x])
        accessLink(link)
        x += 1

    #for sub_heading in soup.find_all('div '):
     #   print(sub_heading.text)

    #name_box = soup.find()
    #print(soup)


if __name__ == "__main__":
    main()
# write your code here
# usage should be python3 part3.py

