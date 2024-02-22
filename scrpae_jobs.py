
import requests
import pandas as pd
import json
import os
import warnings

warnings.filterwarnings("ignore")



directory = r'C:\Users\shivampundir\Downloads\linkedin\efinancials'
os.chdir(directory)
list_of_companies = pd.read_excel(r'list_of_companies.xlsx')


def fetch_job_listings_for_company(company_id):
	url= 'https://job.efinancialcareers.com//api/v1/company/{}/jobs?page_size=500'.format(company_id)
	return requests.get(url,verify=False).json()
	
 
def convert_job_json_to_df(job_json):
	 if 'data' not in job_json:
            return 
	 data = pd.DataFrame(job_json['data'])
	 data['job_url'] =  data.seo_urls.apply(lambda x:x['en_GB'])
	 data['city'] = data.location.apply(lambda x:x['city'])
	 data['country'] = data.location.apply(lambda x:x['country'])
	 return data


def main(list_of_companies):
	list_of_companies = list_of_companies.loc[list_of_companies['city']=='London']
	each_company_job_list = []
	
	for company_number,company_id in enumerate(list_of_companies.id.iloc[:]):
			job_json = fetch_job_listings_for_company(company_id)
			tmp_df = convert_job_json_to_df(job_json)
			if tmp_df is not None:
				print(f' # Companies completed : {company_number+1} , last {company_id} as {len(tmp_df)} listings')
				each_company_job_list.append(tmp_df)
	
	return pd.concat(each_company_job_list,axis=0)
	

if __name__ == "__main__":

	data = main(list_of_companies)
	data.to_excel('scrapped_jobs.xlsx',index=False)