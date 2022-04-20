from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import re

def table_parser():
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    browser = webdriver.Chrome(options=option)
    browser.get('http://cpk.msu.ru/daily/dep_03_bs')
    requiredHtml = browser.page_source
    soup = BeautifulSoup(requiredHtml, 'html5lib')
    table = soup.findChildren('table')
    my_table = table[0]
    rows = my_table.findChildren(['th','tr'])
    output = ''
    for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            value = cell.text
            value = re.findall('\w+ \w+ \w+|\w+ \w+', value)
            if str(value) != '[]':
                output = output + str(value) + '\n'
    output = output.replace("['", "")
    output = output.replace("']", "")
    return output
    

def main():
    msu = table_parser()
    return msu
