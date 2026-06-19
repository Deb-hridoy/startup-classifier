from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from tqdm import tqdm 

urls_dataset = []
base_urls= ["https://betalist.com/browse/productivity/web-tools?page={}"]


for urls in base_urls:
    for page in tqdm(range(1, 132), desc=urls):
        
        driver = webdriver.Chrome()

        url = urls.format(page) 
        driver.get(url)

        time.sleep(2)

        software_urls = driver.find_elements(By.CSS_SELECTOR, "a.absolute.inset-0")
        #href_link = link.get_attribute("href")

        names = driver.find_elements(By.CSS_SELECTOR, "span.dark\\:text-gray-100.shrink-0.leading-snug.font-medium.text-gray-900")
        #name = software_name.text                      dark:text-gray-100 shrink-0 leading-snug font-medium text-gray-900

        mottos = driver.find_elements(By.CSS_SELECTOR, "span.dark\\:text-gray-400.text-base.text-gray-500.lg\\:truncate")
        #motto = software_motto.text                    

        for url, name, motto in zip(software_urls, names, mottos):
            urls_dataset.append({"Software_urls" : url.get_attribute("href"),"Software_Name" : name.text, "Software_Motto" : motto.text})
        #break
        Urls_Dataset = pd.DataFrame(data=urls_dataset)
        Urls_Dataset.to_csv("Dataset_webtools.csv", index=False)
        driver.quit()
        time.sleep(2)
    #break