import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
import time
import os


df = pd.read_csv("Dataset_Url_Startups.csv")

url_list = df["Software_urls"].to_list()

#scrape_list_1 = url_list[97:500]
#scrape_list_1 = url_list[501:1000]
#scrape_list_1 = url_list[1001:1500]      
#scrape_list_1 = url_list[1440:2500]
#scrape_list_1 = url_list[2001:2500]
scrape_list_1 = url_list[2501:3000]
#scrape_list_1 = url_list[3001:3500]
#scrape_list_1 = url_list[3501:4000]
#scrape_list_1 = url_list[4001:4500]
#scrape_list_1 = url_list[4945:5500]
#scrape_list_1 = url_list[5001:5500]
#scrape_list_1 = url_list[7038:]
#scrape_list_1 = url_list[6001:6500]
#scrape_list_1 = url_list[6501:]
#scrape_list_1 = url_list[7001:]

#print(scrape_list[0])
#print(scrape_list[-1])
#print(f"Index : {url_list.index("https://betalist.com/startups/relayknowtify")}")
#print(f"Len:{len(scrape_list)}")
#print(url_list.index("Transor"))
#print(url_list.index("CodeKickBot"))

NLP_Dataset = []

driver = webdriver.Chrome()

for url in tqdm(scrape_list_1):
    
    try:
        driver.get(url)
        
        time.sleep(3)
        # Name
        software_name = driver.find_element(
                    By.CSS_SELECTOR,
                    ".text-xl.sm\\:text-2xl.font-black"
                ).text

        # Motto
        software_motto = driver.find_element(
                    By.CSS_SELECTOR,
                    ".text-base.sm\\:text-lg.text-gray-600.dark\\:text-gray-300"
                ).text

        # Description
        software_description = driver.find_element(
                    By.TAG_NAME,
                    "p"
                ).text

        # Genres
        software_class = driver.find_elements(
                    By.CLASS_NAME,
                    "truncate"
                )

        genres_list = [element.text for element in software_class]

        # Append row
        NLP_Dataset.append({
                    "name": software_name,
                    "motto": software_motto,
                    "description": software_description,
                    "genres": ", ".join(genres_list),
                    "url": url
                })

        # Save immediately after each scrape
        Dataset_nlp = pd.DataFrame(NLP_Dataset)

        Dataset_nlp.to_csv(
                    "Dataset_Url_Startups_NLP_2.csv",
                    index=False
                )
    except:
        print(f"Didn't find the required text:{url}")
    #break
    time.sleep(2)
driver.quit()
print("Scraped for range: (7038: )")