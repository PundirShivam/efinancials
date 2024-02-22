import requests
import pandas as pd
import json
import os
import warnings

warnings.filterwarnings("ignore")

directory = r'C:\Users\shivampundir\Downloads\linkedin\efinancials'
os.chdir(directory)




data_list = []
pg = 1
while True:
	
	url = 'https://job-search-api.efinancialcareers.com/v1/efc/jobs/search?location=London,%20UK&countryCode2=GB&page={}&pageSize=100'.format(pg)
	response = requests.get(url,verify=False)

	json_data = response.json()
	meta_data = json_data['meta']
	
	data = pd.DataFrame(json_data['data'])
	data['city'] = data.jobLocation.apply(lambda x:x['city'])
	data['country'] = data.jobLocation.apply(lambda x:x['country'])
	data['sectors'] = data.sectors.apply(lambda x:','.join(x))
	data_list.append(data)
	current_page = meta_data['currentPage']
	print(f' Completed page number {current_page}')
    pg = pg + 1
	if pg > meta_data['pageCount']:
        break
		
		
jobs_df = pd.concat(data_list,axis=0)
jobs_df = jobs_df.reset_index(drop=True)
jobs_df['jobUrl'] = 'https://www.efinancialcareers.co.uk'+jobs_df['detailsPageUrl']
jobs_df.to_excel('London-Jobs.xlsx')