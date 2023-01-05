from asyncio import streams
from email.mime import image
from multiprocessing.sharedctypes import Value
import shutil
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import requests

# another import
import os
import wget as wget

def ambil_foto(parameter):
    driver = webdriver.Chrome('E:/chromedriver_win32/chromedriver.exe')
    #driver = webdriver.Chrome() if your chromedriver.exe inside root

    driver.get("https://shopee.co.id/search?keyword="+parameter)

    driver.execute_script("window.scrollTo(0, 4000);")

    images = driver.find_elements(By.XPATH, '//img[@class="_7DTxhh vc8g9F"]')
    images = [image.get_attribute('src') for image in images]

    path = 'Shoppe_scraping/' 
    path = os.path.join(path, parameter[0:])
    os.makedirs(path,exist_ok=True)


    counter = 0
    for images2 in images:
        save_as = os.path.join(path, parameter[0:] + str(counter) + '.jpeg')
        wget.download(images2, save_as)
        
        if counter == 10:
            break
        counter += 1