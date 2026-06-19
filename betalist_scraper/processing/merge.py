import pandas as pd
"""
dataset_names = [
    "Dataset_recruiting", "Dataset_social-fundraising", "Dataset_sales_automation", 
    "Dataset_tracking", "Dataset_crm", "Dataset_ai-image-creation",
    "Dataset_ai-chat", "Dataset_Url_Startups"
]

all_dfs = []
#for i in range(6, 20):
for dataset in dataset_names:
    df = pd.read_csv(f"{dataset}_NLP.csv")
    all_dfs.append(df)
df_merge = pd.concat(all_dfs, ignore_index=False)
df_merge.to_csv("Dataset__Merge__NLP.csv", index=False)
df = pd.read_csv("Dataset__Merge__NLP.csv")
print(len(df))
"""
df_1 = pd.read_csv("Merge_NLP_Dataset_First.csv")
df_2 = pd.read_csv("Dataset__Merge__NLP.csv")
#df_3 = pd.read_csv("Dataset_Url_Startups_NLP_3.csv")

df = pd.concat([df_1, df_2], ignore_index=True)
df.to_csv("Startups_Dataset_Merge.csv", index=False)
print(len(df))
