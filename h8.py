import json
"""
QT 1
func name averagePopulation()
take in geographical bloc 
return average population in the bloc
"""
def averagePopulation(bloc):
    pop = 0
    count = 0
    with open("data.json", 'r') as file:
        world = json.load(file)
    for i in range(len(world)):
        try:
            if world[i]["regionalBlocs"][0]["acronym"] == bloc:
                pop += float(world[i]["population"])
                count +=1
        except KeyError as e:
            continue
    return pop/count
##print(averagePopulation("EFTA"))
"""
QT 2 
func name commonCountries
take in two tuple of language 
return countires who speak both languages
"""
def commonCountries(langOne, langTwo):
    result = []
    count = 0
    with open("data.json") as file:
        world = json.load(file)
    for i in range(len(world)):
        try:
            langs = world[i]["languages"]
            for lang in langs:
                if langOne[1] == lang["name"] or langTwo[1] == lang["name"]:
                    count +=1
        except KeyError as e: 
            continue
        if count == 2:
            result.append(world[i]["name"])
        count = 0
    return result
##print(commonCountries(("en", "English"),("es", "Spanish")))
"""
QT 3 
func name uniqueRegions()
take in country list 
return true if all countries are located in different regions 
false if they are in the same region
"""
def uniqueRegions(countryList):
    regionDict = {}
    with open("data.json") as file:
        world = json.load(file)
        for i in range(len(world)):
            try:
                regionDict[world[i]["cioc"]] = world[i]["region"]
            except KeyError as e:
                continue
        region = ""
        for country in countryList:
            try:
                if len(region) == 0:
                    region = regionDict[country.upper()]
                if not region == regionDict[country.upper()]:
                    return False
            except KeyError:
                return "Invalid Country!"
    return True
##print(uniqueRegions(["usa","adsf" "ger"]))
"""
QT 4 
func name oraganizeCapitals()
take in capitalList 
return a dictionary mapping regions to countries
"""
def organizeCapitals(capitalList):
    result = {}
    map = {}
    with open("data.json") as file:
        world = json.load(file)
        for i in range(len(world)):
            try:
                capital = world[i]["capital"]
                for cap in capital.split(", "):
                    map[cap] = [world[i]["name"], world[i]["region"]]
            except KeyError:
                continue
        for capital in capitalList:
            try:
                region = map[capital][1]
                country = map[capital][0]
                if region not in result:
                    result[region] = [country]
                else:
                    countryList = result[region]
                    countryList.append(country)
                    result[region] = countryList
            except KeyError as e :
                continue
    return result
##print(organizeCapitals((["Beijing", "Washington", "Jakarta"])))
"""
QT 5
func name visitableCountries
take in list of country codes
you visited from country in given order 
you can visit if country share a border
return countries you can visit 
"""
def visitableCountries(codeList):
    result = []
    map = {}
    with open("data.json") as file:
        world = json.load(file)
        for i in range(len(world)):
            try:
                map[world[i]["alpha3Code"]] = [world[i]["name"], world[i]["borders"]]
            except KeyError:
                continue
        prev = ""
        for code in codeList:
            if len(result) == 0:
                result.append(map[code][0])
            else:
                for border in map[prev][1]:
                    if border == code:
                        result.append(map[code][0])
            prev = code
    return result
print(visitableCountries(["NGA", "BEN", "COL"]))
