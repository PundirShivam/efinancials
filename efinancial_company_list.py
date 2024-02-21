
import json
import pandas as pd
import os

directory = r'..\linkedin\efinancials'
os.chdir(directory)
json_file = "efinancial.json"

# Open the JSON file with the correct encoding
with open(json_file, 'r', encoding='utf-8') as file:
    # Load JSON data
    data = json.load(file)

data = data['data']
data = pd.DataFrame(data)

data['company_url'] = r'https://www.efinancialcareers.co.uk/companies/'+ data.urlSubPath
data['industry']    = data['industry'].apply(lambda x:x['id'])
data.to_excel(r'list_of_companies.xlsx')
