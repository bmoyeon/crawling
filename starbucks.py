import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

f = open('starbucks.csv', 'w+', encoding='utf-8')
cw = csv.writer(f)
cw.writerow(['menu', 'image'])

driver = webdriver.Chrome('/Users/user/Downloads/chromedriver')
driver.get('https://www.starbucks.co.kr/menu/drink_list.do')

html = driver.page_source
bs = BeautifulSoup(html, 'html.parser')
infos = bs.select('a.goDrinkView')

for info in infos:
    menu = info.select('img')[0]['alt']
    image = info.select('img')[0]['src']
    
    cw.writerow( (menu, image) )

f.close()
driver.quit()