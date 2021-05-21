from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

startUrl = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('chromedriver')
browser.get(startUrl)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
time.sleep(10)

def scrape():
    headers = ["Name", "Distance","Mass","Radius"]
    planetData = []
    for i in range (0-439):
        soup = BeautifulSoup(browser.page_source,'html.parser')
        for ul_tag in soup.find_all('ul',attrs={'class',"stars"}):
            li_tags = ul_tag.find_all('li')
            tempList = []
            for index,li_tag in enumerate(li_tags):
                if index == 0:
                    tempList.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        tempList.append(li_tag.contents[0])
                    except:
                        tempList.append("")
            planetData.append(tempList)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        with open("scraper_2.csv","w") as f:
            csvWriter = csv.writer(f)
            csvWriter.writerow(headers)
            csvWriter.writerows(planetData)
            
scrape()