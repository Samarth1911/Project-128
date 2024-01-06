from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import  BeautifulSoup 
import pandas as pd 
import time
import requests

Start_Url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome()
browser(Start_Url)

time.sleep(10)

new_stars_data = []

def scrape_more_data(hyperlink):
    try:
        print(hyperlink)
        page = requests(hyperlink)
        soup = BeautifulSoup(page.content, "html.parser")
        temp_list = []

        for tr_tags in soup.find_all("tr"):
             td_tags = tr_tags.find_all("td")
             for td_tag in td_tags :
              try: 
                temp_list.append(td_tag,[0].content[0])
              except:
                 temp_list.append("")
        
        new_stars_data.append(temp_list)
    except:
        time.sleep(1)
scrape_more_data()

stars_df_1 = pd.read_csv("Stars.csv")

scrapped_data = []

for row in new_stars_data:
   replaced = []
   for i in row :
     i.replace("\n","")
     replaced.append(i)

   scrapped_data.append(replaced)
print(scrapped_data)

header = ["Stars_name","Mass","Radius","Distance"]

new_stars_df_1 = pd.DataFrame(scrapped_data, columns = header)

new_stars_df_1.to_csv("New_stars.csv", index = True , index_label = "id")



   









