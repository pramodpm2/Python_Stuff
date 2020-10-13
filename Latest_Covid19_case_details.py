from covid import Covid
from datetime import datetime as dt
def covidUpdateSpecificCountry(i_country):
	specific_country=Covid().get_status_by_country_name(i_country)
	active=specific_country['active']
	confirmed=specific_country['confirmed']
	recovered=specific_country['recovered']
	deaths=specific_country['deaths']
	time=specific_country['last_update']
	data_updated_at=dt.fromtimestamp(time/1000)
	print('\n '+i_country + ' COVID INFORMATION : \n')
	print('	TOTAL ACTIVE : '+str(active))
	print('	TOTAL CONFIRMED : '+str(confirmed))
	print('	TOTAL RECOVERED : '+str(recovered))
	print('	TOTAL DEATHS : '+str(deaths))
	print('	LAST UPDATED AT : '+str(data_updated_at))


if __name__=='__main__':
	
	print('\n GET LATEST COVID19 CASES DETAILS  IN SPECIFIC COUNTRY : ')
	country=input('\n\n ENTER THE COUNTRY NAME : ')
	covidUpdateSpecificCountry(country)
