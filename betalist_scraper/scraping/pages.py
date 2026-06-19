from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from tqdm import tqdm 


#base_urls= ["https://betalist.com/browse/other/startups?page={}", "https://betalist.com/browse/productivity/business-services?page={}", "https://betalist.com/browse/productivity/services?page={}", "https://betalist.com/browse/other/technology?page={}"]
base_urls= ["https://betalist.com/browse/sales/crm?page={}",
            "https://betalist.com/browse/ai/ai-chat?page={}",
            "https://betalist.com/browse/data-analytics/tracking?page={}",
            "https://betalist.com/browse/data-analytics/real-time?page={}",
            "https://betalist.com/browse/media-content/guides?page={}",
            "https://betalist.com/browse/finance/social-fundraising?page={}",
            "https://betalist.com/browse/finance/angel-investing?page={}",
            "https://betalist.com/browse/ai/ai-development?page={}"]

# 21
driver = webdriver.Chrome()

for base_url in base_urls:

    urls_dataset = []

    for page_urls in tqdm(range(1, 16), desc=base_url):
        try:
            page_url = base_url.format(page_urls)
            driver.get(page_url)

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
            category = base_url.split("/")[-1].split("?")[0]
            Urls_Dataset = pd.DataFrame(data=urls_dataset)
            Urls_Dataset.to_csv(f"Dataset_{category}.csv", index=False)
        except Exception as e:
            print(f"Didn't find {page_urls} : e")
        time.sleep(2)
        #break
driver.quit()
    #break