import requests
from datetime import datetime, timedelta
import logging


# Client for swiss covid 19 data
class CovidClient:
    def __init__(self):
        self.log = logging.getLogger('CovidClient')

    def get_covid_data(self, covid_data_request):
        if covid_data_request.date:
            return self._get_covid_data_by_date(covid_data_request.canton, covid_data_request.date)
        else:
            return self._get_latest_covid_data(covid_data_request.canton)

    # Get covid 19 data by date and canton
    def _get_covid_data_by_date(self, canton, date):
        response = requests.get(
            'https://covid19-rest.herokuapp.com/api/openzh/v1/country/CH/area/' + canton + '?date=' + date,
            auth=('', '')).json()
        return response['records'][len(response['records']) - 1]

    # Get latest covid 19 data for canton
    def _get_latest_covid_data(self, canton):
        delta = 1
        while True:
            response = self._get_covid_data_by_date(canton,
                                                    datetime.strftime(datetime.now() - timedelta(delta), '%Y-%m-%d'))
            delta = delta + 1
            if 'time' in response:
                break
        return response
