import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
import time
import os


dataset_name = [
    #"Dataset_recruiting", 
    #"Dataset_social-fundraising", 
    #"Dataset_sales_automation", 
    #"Dataset_tracking", 
    #"Dataset_crm", "Dataset_ai-image-creation", "Dataset_ai-chat", "Dataset_ai_tools", 
    "Dataset_Url_Startups"
]

#dataset_name = [
    #"Dataset_APIs", "Dataset_B2B"
#]

for dataset in tqdm(dataset_name, desc="Processing datasets"):

    driver = webdriver.Chrome()

    # Store rows for this dataset
    NLP_Dataset = []

    # Read URLs CSV
    df = pd.read_csv(f"{dataset}.csv")

    dataset_urls = df["Software_urls"].tolist()

    output_file = f"{dataset}_NLP.csv"

    for url in tqdm(dataset_urls, desc=dataset, leave=False):

        #driver = None
        try:
            # Open browser

            driver.get(url)

            time.sleep(2)

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
                output_file,
                index=False
            )

            #print(f"Saved: {software_name}")
            time.sleep(2)
        except Exception as e:
            print(f"Error scraping {url}: {e}")

        #finally:
            # Close browser every URL
            #if driver:
    driver.quit()