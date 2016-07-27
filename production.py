#!/usr/local/bin/python2.7
from lxml import html
from selenium import webdriver
# import pandas as pd


driver = webdriver.PhantomJS(executable_path='/home/droz/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

driver.get("http://apps.marincounty.org/BookingLog/")

button = driver.find_element_by_xpath('''//*[@id="no-sidebar-main-content"]/div[2]/form/div/div[2]/input[1]''')
button.click()
page = driver.page_source.encode('utf-8')

tree = html.fromstring(page)

names = tree.xpath('''//*[@id="sec1"]/h2/text()''')
addresses = tree.xpath('''//*[@id="sec1"]/div[1]/table/tbody/tr[2]/td/text()''')
addresses = [ad.strip('\n').strip() for ad in addresses]
booking_links = tree.xpath('''//*[@id="sec3"]/a''')
booking_links = [booking_links[i].attrib['href'] for i in range(len(booking_links))]

with open("/home/droz/for/jenna/output.csv", "a") as f:
    f.write('\n'.join('`'.join(x) for x in list(zip(names, addresses, booking_links))))
