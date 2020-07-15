from bs4 import BeautifulSoup
import requests
source = requests.get('https://concreteplayground.com/auckland/shops').text
soup=BeautifulSoup(source,'lxml')

for article in soup.find_all('article'):
    #print(article.prettify())
    headline=article.a.text
    print(headline)
    summary=article.find('div',class_='title').a.text
    print(summary)
    print()

for link in soup.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

for name in soup.find_all('li',class_='item venuebox icon-variant-gold clearfix'):
    lat=soup.find('li',class_='item venuebox icon-variant-gold clearfix')['data-latitude']
    print(lat)
    long=soup.find('li',class_='item venuebox icon-variant-gold clearfix')['data-longitude']
    print(long)

    shops=name.find('div',class_='info clearfix').a.text
    print(shops)
    print()
    

                                                                          
