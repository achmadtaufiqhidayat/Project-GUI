import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

images = []

driver = webdriver.Chrome(r'C:/Users/Tegar/chromedriver.exe')
driver.get('https://shopee.co.id/mall/search?keyword=samsung')
time.sleep(5)
for i in range(10):
    driver.execute_script("window.scrollBy(0, 350)")
    time.sleep(1)

content = driver.page_source
soup = BeautifulSoup(content)

for item in soup.select('div[data-sqe="item"]'):
    dataImg = item.find('img', class_="_7DTxhh vc8g9F")
   

    if dataImg is not None:
       
        images.append(dataImg['src'])

df = pd.DataFrame(
  
 { 'Images': images})
print(df)
df.to_csv('scraping.txt',index=False)



