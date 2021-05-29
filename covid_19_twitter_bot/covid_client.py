import requests
from datetime import datetime, timedelta

def getCovidDataCantonDate(canton, date):
    r = requests.get('https://covid19-rest.herokuapp.com/api/openzh/v1/country/CH/area/' + canton + '?date=' + date, auth=('', ''))
    response = r.json()
    return response['records'][len(response['records']) - 1]

def getCovidDataCantonNew(canton):
    delta = 1
    while True:
        response = getCovidDataCantonDate(canton, datetime.strftime(datetime.now() - timedelta(delta), '%Y-%m-%d'))
        delta = delta + 1
        if 'time' in response:
            break
    return response



covidData = getCovidDataCantonDate('ZH', '2021-05-17')
print(covidData['current_hosp'])

covidData = getCovidDataCantonNew('ZH')
print(covidData['current_hosp'])