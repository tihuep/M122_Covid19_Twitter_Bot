import requests

def getCovidData(canton, date):
    r = requests.get('https://covid19-rest.herokuapp.com/api/openzh/v1/country/CH/' + ('area/' + canton if canton != '' else '') + ('?date=' + date if date != '' else ''), auth=('', ''))
    response = r.json()
    return response['records'][0]

"""
covidData = getCovidData('ZH', '2021-05-14')
print(covidData['current_hosp'])
"""