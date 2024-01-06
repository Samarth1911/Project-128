from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import  BeautifulSoup 
import pandas as pd 
import time 

Start_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

#WebDriver
browser = webdriver.Chrome("C:\Users\Satyam\Desktop\My coding projects\Project 127\chromedriver.exe")
browser.get(Start_URL)

time.sleep(10)

scrape_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    bright_stars_body = soup.find("table", attrs = {"class","table"})
    table_body = bright_stars_body.find("tbody")
    table_rows = table_body.find_all("tr")

    temp_list = []

    for row in table_rows :
        table_cols = row.find_all("td")
        print(table_cols)

        for cols in table_cols:
            data = cols.text.strip()
            temp_list.append(data)

    scrape_data.append(temp_list)

stars_data = []

for i in range(0,len(scrape_data)):
    Stars_name = scrape_data[i][1]
    Distance = scrape_data[i][3]
    Mass = scrape_data[i][5]
    Radius = scrape_data[i][6]
    Lun = scrape_data[i][7]

    required_data = [Stars_name,Distance,Mass,Radius,Lun]
    stars_data.append(required_data)

#Define Header 
header = ['Stars_name','Distance','Mass','Radius','Lun']

#Define pandas Dataframe 
stars_df_1 = pd.DataFrame(stars_data, columns = header)

#convert to csv
stars_df_1.to_csv("Stars.csv", index = True, index_label='id')


  
  
  
  

  
        








