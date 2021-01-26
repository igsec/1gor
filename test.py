import requests
from bs4 import BeautifulSoup

rozetka = 'https://rozetka.com.ua/ua/krupy/c4628397/vid-225787=grechka/'
fozzy = 'https://fozzyshop.ua/ru/300143-krupa-grechnevaya/s-15/kategoriya-krupa_grechnevaya'
bigl = 'https://bigl.ua/search?search_term=%D0%BA%D1%80%D1%83%D0%BF%D0%B0&category=20521'

def parseRozetka():
    response = requests.get(rozetka)
    soup = BeautifulSoup(response.content, 'lxml')
    records=soup.findAll('div', class_ = 'goods-tile')
    name=['Rozetka']
    som = []
    for item in records:
        if '1кг' in item.find('a', class_ = 'goods-tile__heading').get_text(strip=True) \
                or '1 кг' in item.find('a', class_ = 'goods-tile__heading').get_text(strip=True) \
                or '1,0 кг' in item.find('a', class_ = 'goods-tile__heading').get_text(strip=True) :
            som.append({
                'title':item.find('a', class_ = 'goods-tile__heading').get_text(strip=True) ,
                'cost': item.find('span', class_ = 'goods-tile__price-value').get_text(strip=True) + ' грн',
                'href': item.find('a', class_='goods-tile__heading').get('href')
            })
    return som

def parseFozzy():
    response = requests.get(fozzy)
    soup = BeautifulSoup(response.content, 'lxml')
    records = soup.find_all('article', class_='product-miniature product-miniature-default product-miniature-grid product-miniature-layout-1 js-product-miniature')
    som=[]
    for item in records:
        if '1кг' in item.find('div', class_='product-reference text-muted').get_text(strip=True)\
                or '1000г' in item.find('div', class_='product-reference text-muted').get_text(strip=True):
            som.append({
                'title':item.find('div', class_='h3 product-title').get_text(strip=True),
                'cost': item.find('span', class_='product-price').get_text(strip=True),
                'href': item.find('a', class_='thumbnail product-thumbnail').get('href')
            })
    return som

def parseBigl():
    response = requests.get(bigl)
    soup = BeautifulSoup(response.content, 'lxml')
    records = soup.find_all('div',class_='bgl-product__body')
    som=[]
    for item in records:
        if '1 кг' in item.find('span', class_='translate').get_text(strip=True):
            som.append({
                'title': item.find('span', class_='translate').get_text(strip=True),
                'cost': item.find('div', class_='bgl-product-price__item').get_text(strip=True),
                'href': item.find('a', class_='bgl-product__title').get('href')
            })
    return som