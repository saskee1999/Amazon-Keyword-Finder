from selenium import webdriver
from pprint import pprint
browser = webdriver.Chrome('./chromedriver.exe')
import time
browser.get('https://www.amazon.com/s?i=specialty-aps&bbn=16225006011&rh=n%3A%2116225006011%2Cn%3A11060451&ref=nav_em_0_2_18_3__nav_desktop_sa_intl_skin_care')

wfreq = {}

for iteration in range(10):

    time.sleep(5)

    it = browser.find_elements_by_class_name('a-size-base-plus')

    for i in it:
        i = i.find_elements_by_class_name('a-color-base')

    for i in it:
        i = i.find_elements_by_class_name('a-text-normal')

    for i in it:
        text = i.text
        words = text.split()
        for word in words:
            if word not in wfreq:
                wfreq[word]=0
            wfreq[word]+=1

    nxtbutton = browser.find_element_by_class_name('a-last')
    nxtbutton = nxtbutton.find_element_by_tag_name('a')
    nxtbutton.click()

time.sleep(5)

it = browser.find_elements_by_class_name('a-size-base-plus')

for i in it:
    i = i.find_elements_by_class_name('a-color-base')

for i in it:
    i = i.find_elements_by_class_name('a-text-normal')

for i in it:
    text = i.text
    words = text.split()
    for word in words:
        if word not in wfreq:
            wfreq[word]=0
        wfreq[word]+=1

pprint(wfreq)

