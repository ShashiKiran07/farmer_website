
def find_weather():
    codes = {'kanagarthi': '2827345'}
    url = "https://www.accuweather.com/en/in/" + 'kanagarthi' + "/" + codes['kanagarthi'] +\
     "/current-weather/" + codes['kanagarthi']
    return url