import re
from covid_data_request import CovidDataRequest

request_pattern_regex = \
    r"^covid[ \t]+([A-Z]{2})(?:[ \t]+((?:3[01]|[12][0-9]|0[1-9])-(?:1[0-2]|0[1-9])-[0-9]{4}))?[ \t]*$"


def parse(covid_data_request_string):
    result = re.search(request_pattern_regex, covid_data_request_string)
    if not result:
        return None
    groups = result.groups()
    if len(groups) == 2:
        return CovidDataRequest(
            canton=groups[0],
            date=groups[1])
    else:
        return CovidDataRequest(
            canton=groups[0])
