from bs4 import BeautifulSoup
import shutil
import requests
import os

manga = ('Boku no Hero Academia','Tales of Demons and Gods','Yahalue','')

os.chdir('..\..\Desktop\Manga')
def folder():
    for f in manga:
        if f not in os.listdir():
            os.makedirs(f)

def image_downloader(url):

    url = requests.get(url)
    source_code = url.text
    soup = BeautifulSoup(source_code, 'html.parser')
    temp = soup.title.string + ".jpg"
    if temp not in os.listdir():
        image_link = soup.find('img', {'id': 'image'}).get('src')
        r = requests.get(image_link, stream=True, headers={'User-agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            with open(temp, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

def downloader(url):
    base = url[:url.rfind('/')]
    link = requests.get(url)
    source_code = link.text
    soup = BeautifulSoup(source_code,'html.parser')
    temp = soup.find("a",{'class': "next_page"})
    while temp != None:
        image_downloader(url)
        url = soup.find("a",{'class': "next_page"}).get('href')
        print(url )
        link = requests.get(url)
        source_code = link.text
        soup = BeautifulSoup(source_code,'html.parser')

def manga_updater(url):
    url = requests.get(url)
    source_code = url.text
    soup = BeautifulSoup(source_code,'html.parser')
    for f in manga:
        temp = soup.find('a',{'rel':f})
        while temp != None:
            nw = temp.next_sibling.parent.next_sibling.next_element
            downloader(nw.get('href'))



manga_updater("http://www.mangahere.co/")
folder()
# downloader("http://www.mangahere.co/manga/boku_no_hero_academia/c098/5.html")



 # image_downloader('http://www.mangareader.net/world-trigger/148', r'C:\Users\Acer\PycharmProjects\Web Crawler\Test')