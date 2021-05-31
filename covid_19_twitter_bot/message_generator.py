# Format covid data message
def generate_response_message(data):
    try:
        message = str(data['date']) + ' ' + str(data['time']) + ', ' + str(data['abbreviation_canton_and_fl']) + ': ' + str(data['current_hosp']) + ' Hospitalisierte, ' + str(data['current_isolated']) + ' Isolierte und ' + str(data['current_quarantined']) + ' In Quarantäne. (' + str(data['source']) + ')'
    except:
        message = 'Es wurden zu dieser Selektion keine Daten gefunden.'

    return message

# Format wrong syntax message
def wrong_syntax():
    return 'Die Syntax entspricht nicht den Anforderungen: covid kanton [datum]. z.B. covid ZH 2021-05-18'