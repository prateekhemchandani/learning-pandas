import pandas as pd

df_csv = pd.read_csv('sales_data_sample.csv', encoding="latin1")
print(df_csv)

df_xlsx = pd.read_excel('SampleSuperstores.xlsx', engine='openpyxl')
print(df_xlsx)

df_json = pd.read_json('sample_Data.json')
print(df_json)