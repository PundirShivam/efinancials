import requests
import time
import warnings
warnings.filterwarnings("ignore")

headers = {
    'authority': 'job-search-api.svc.dhigroupinc.com',
    'method': 'GET',
    'path': '/v1/dice/jobs/search?locationPrecision=City&latitude=32.7766642&longitude=-96.79698789999999&countryCode2=US&radius=30&radiusUnit=mi&page=2&pageSize=100&facets=employmentType%7CpostedDate%7CworkFromHomeAvailability%7CworkplaceTypes%7CemployerType%7CeasyApply%7CisRemote%7CwillingToSponsor&fields=id%7CjobId%7Cguid%7Csummary%7Ctitle%7CpostedDate%7CmodifiedDate%7CjobLocation.displayName%7CdetailsPageUrl%7Csalary%7CclientBrandId%7CcompanyPageUrl%7CcompanyLogoUrl%7CcompanyLogoUrlOptimized%7CpositionId%7CcompanyName%7CemploymentType%7CisHighlighted%7Cscore%7CeasyApply%7CemployerType%7CworkFromHomeAvailability%7CworkplaceTypes%7CisRemote%7Cdebug%7CjobMetadata%7CwillingToSponsor&culture=en&recommendations=true&interactionId=0&fj=true&includeRemote=true&eid=100478416_1004190344',
    'scheme': 'https',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Origin': 'https://www.dice.com',
    'Priority': 'u=1, i',
    'Referer': 'https://www.dice.com/',
    'Sec-Ch-Ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'X-Api-Key': '1YAt0R9wBg4WfsF9VB2778F5CHLAPMVW3WAZcKd8'
}

pg = 1
data_list = []
while True:
	url = f'https://job-search-api.svc.dhigroupinc.com/v1/dice/jobs/search?locationPrecision=City&latitude=32.7766642&longitude=-96.79698789999999&countryCode2=US&radius=30&radiusUnit=mi&page={pg}&pageSize=100&facets=employmentType%7CpostedDate%7CworkFromHomeAvailability%7CworkplaceTypes%7CemployerType%7CeasyApply%7CisRemote%7CwillingToSponsor&fields=id%7CjobId%7Cguid%7Csummary%7Ctitle%7CpostedDate%7CmodifiedDate%7CjobLocation.displayName%7CdetailsPageUrl%7Csalary%7CclientBrandId%7CcompanyPageUrl%7CcompanyLogoUrl%7CcompanyLogoUrlOptimized%7CpositionId%7CcompanyName%7CemploymentType%7CisHighlighted%7Cscore%7CeasyApply%7CemployerType%7CworkFromHomeAvailability%7CworkplaceTypes%7CisRemote%7Cdebug%7CjobMetadata%7CwillingToSponsor&culture=en&recommendations=true&interactionId=0&fj=true&includeRemote=true&eid=100478416_100419034'
	response = requests.get(url, headers=headers,verify=False)
	if response.status_code!=200:
		break
	json = response.json()
	df_tmp = pd.DataFrame(json['data'])
	data_list.append(df_tmp)
	
	print(f"Completed page number {json['meta']['currentPage']}")
	if json['meta']['currentPage'] == json['meta']['pageCount']:
		print('Completed')
		break
	pg = pg + 1
	time.sleep(1)
	
data = pd.concat(data_list,axis=0)
data = data.reset_index(drop=True)
data.to_excel(r'C:\Users\shivampundir\Downloads\linkedin\JobsInDallasTexas_27May2024.xlsx')