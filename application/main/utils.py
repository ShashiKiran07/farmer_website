
def find_weather(region,code):
    # codes = {'kanagarthi': '2827345'}
    # if region in codes.keys():
    url = "https://www.accuweather.com/en/in/" + region + "/" + code +\
     "/current-weather/" + code
    return url
    # else:
    #     return ("/homepage")

location_codes = {'kanagarthi': '2827345', 'kanukula': '2827318', 'karimnagar' : '186804', 'sultanabad': '2827152', 'mancharami': '2827453',\
    'elgaid' : '2827095', 'julapalle': '2826889', 'choppadandi':'2827022', 'kadambapur': '2827307', 'suddala':'2827230','odela':'2827374',\
        'kolanoor': '2827231' }