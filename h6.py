"""
QT 6
func name findTicket()
take in ticket dictionary
return cheapest ticket tuple
"""
def findTicket(map):
    if len(map) == 0:
        return "No tickets available!"
    min = float('inf')
    city = ""
    keys = map.keys()
    for key in keys:
        if map.get(key) < min:
            city = key
            min = map.get(key)
    result = (city, min)
    return result
##print(findTicket({}))
"""print(findTicket( {
"Air Seoul" : 700,
"Asiana Airlines" : 500,
"China Eastern" : 900,
"Frontier" :1000
}))"""
"""
QT 2 
func name findHotel()
take in hotel dict
reutrn preffered hotel given the dict
"""
def findHotel(map):
    if len(map) == 0:
        return "No hotels Available!"
    result = {}
    freq = {}
    keys = map.keys()
    for key in keys:
        try:
            if not map.get(key) in freq:
                freq[map.get(key)] = 1
            else:
                prev = freq[map.get(key)]
                freq[map.get(key)] = prev + 1
        except TypeError as e:
            return "Invalid hotel prefernce encountered!"
    key = ""
    for hotel in freq:
        try:
            if len(result) == 0:
                key = hotel
                result[key] = freq[hotel]
            if freq[hotel] > result[key]:
                key = hotel
                result[key] = freq[hotel]
        except Exception as e:
            return "Processing error!"
    return result
"""print(findHotel(   {
"Arvin" : "Grand Hyatt Beijing",
"Craig" : "Grand Millennium Beijing",
"Josh": "Grand Hyatt Beijing"
}))"""
"""
QT 3
func name findEvent()
take in list of interst and dict of schedule
return list of days are your interest
"""
def findEvent(interests, schedule):
    result = []
    for key in schedule.keys():
        for event in schedule.get(key):
            for interest in interests:
                if event == interest and key not in result:
                    result.append(key)
    result.sort()
    return result
"""print(findEvent(["Luge","Ski Jumping","Figure Skating"],  {
"Feb 18" : ["Skiing","Snowboard","Luge"],
"Feb 19" : ["Skeleton", "Ski Jumping"],
"Feb 20" : ["Skiing","Curling"]
}))"""
"""
QT 4
func name figureSkating()
take in technical scores and component scores
add the two scores in the same index taht do not give errors
return lsit of final scores
"""
def figureSkating(tech, comp):
    result = []
    tp = 0
    cp = 0
    while(tp < len(tech) and cp < len(comp)):
        try:
            sum = tech[tp] + comp[cp]
            result.append(sum)
        except TypeError as e:
            tp+=1
            cp +=1
        else:
            tp +=1
            cp+=1
    return result
##print(figureSkating([100, "&", 110, 130, 110], ["*", 120, 110, 130, 130]))
"""
QT 5
func name sportManagement()
take in dict of         country - > [sports]
return dict of          sports -> [country]
"""
def sportManagement(countryDict):
    sportDict = {}
    for country in countryDict.keys():
        for sport in countryDict.get(country):
            if sport not in sportDict:
                countryList = [country]
                sportDict[sport] = countryList
            else:
                countryList = sportDict[sport]
                countryList.append(country)
                countryList.sort()
                sportDict[sport] = countryList

    return sportDict
print(sportManagement( {"Belarus": ["Ice Hockey", "Skiing"],
"Lebanon": ["Skiing", "Snowboard"],
"Denmark":["Skiing", "Luge"]}))