from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import re


service = Service(executable_path="usr/local/bin/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# create scraped list elements
amiibo_name = []
amiibo_series = []
release_date = []

driver.get("https://www.nintendo.com/amiibo/line-up/")


# scrape amiibo data
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('div', attrs={'class':'BasicTilestyles__Container-sc-1bsju6x-0 hKftmL'}):
    name          = a.find('h1', attrs={'class':'Headingstyles__StyledH-sc-s17bth-0 dznSLt'})
    series        = a.find('p', attrs={'class':'Textstyles__StyledCaption-sc-w55g5t-1 eUAJWi'})
    date          = a.find(text=re.compile('^Available'))
    amiibo_name.append(name.text)
    amiibo_series.append(series.text)
    release_date.append(date.text)

amiibo_df = pd.DataFrame({'amiibo_name':amiibo_name,
                          'amiibo_series':amiibo_series,
                          'release_date':release_date})


print(amiibo_df)


#-----------------------------------------

# export to excel
amiibo_df.to_excel('/Users/drad/Documents/Data_Projects/Amiibo_Dashboard/amiibo_list.xlsx', index=False)