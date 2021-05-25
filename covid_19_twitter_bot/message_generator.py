def generateResponseMessage(data):
    if (data == None): return 'No Data'
    return str(data['date']) + ' ' + str(data['time']) + ', ' + str(data['abbreviation_canton_and_fl']) + ': ' + str(data['current_hosp']) + ' Hospitalisierte, ' + str(data['current_isolated']) + ' Isolierte und ' + str(data['current_quarantined']) + ' In Quarantäne. (' + str(data['source']) + ')'