 #! /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox() # Get local session of firefox
browser.get("http://218.108.6.116:8080/zxjc/datashow_getdatashowhtml?wrlx=1&xzqy=330100&x=41&y=11&sjlx=day12&kssj=2012-1-1%2C00") # Load page
#assert "Yahoo!" in browser.title [contains(@value='下一页')]
elem = browser.find_element_by_tag_name("td") # Find the query box
elem.send_keys("seleniumhq" + Keys.RETURN)
time.sleep(0.2) # Let the page load, will be added to the API
try:
    browser.find_element_by_xpath("//input").click()
    browser.getPageSource()
    toString()
except NoSuchElementException:
    assert 0, "can't find seleniumhq"
browser.close()
