import csv 

"""
QT 1
func name findCuisine()
given a filename and cuisine favorite
return resturant with given cuisine type fav
"""
def findCuisine(filename, cuisine):
    prev  = ""
    result = []
    with open("resturant.txt", "r") as file:
        print("a")
        for line in file:
            if(line.strip() == cuisine):
                result.append(prev)
            prev = line.rstrip()
    return result        
##print(findCuisine("resturant.txt", "Amaesrican"))
"""
QT 2
func name resturantFilter()
take in file name 
return dict of cuisiene mapped to resturant
"""
def restaurantFilter(filename):
    prev = ""
    map = {}
    counter = 0
    with open(filename) as file:
        for i, line in enumerate(file):
            cur = line.rstrip()
            if i == 1 or counter == 4:
                if cur not in map:
                    map[cur] = [prev]
                else:
                    l = map.get(cur)
                    l.append(prev)
                    map[cur] = l
                counter = 0
            counter +=1
            prev = cur
    return map
"""
QT 3
func name createDirectory()
take in filename and ouputfilename
return txt file that has directory, 
fast food
1. name ->type

Sit-down
1.name - >type
"""
def createDirectory(filename, output):
    f = []
    s = []
    with open(filename) as file:
        prevTwo = []
        for line in file:
            cur = line.rstrip()
            if cur == "Fast Food":
                f.append({"restaurant":prevTwo[0], "type": prevTwo[1]})
                prevTwo.clear()
            elif cur == "Sit-down":
                s.append({"restaurant":prevTwo[0], "type": prevTwo[1]})
                prevTwo.clear()
            else:
                if not len(cur) == 0:
                    prevTwo.append(cur)
    with open(output, "a") as result:
        result.write("Restaurant Directory\n\n") 
        result.write("Fast Food\n")
        for i,item in enumerate(f):
            result.write(f"{i+1}. {item["restaurant"]} - {item["type"]}\n")
        result.write("\n")
        result.write("Sit-down\n")
        for i, item in enumerate(s):
            if i +1 < len(s):
                result.write(f"{i+1}. {item["restaurant"]} - {item["type"]}\n")
            else:
                result.write(f"{i+1}. {item["restaurant"]} - {item["type"]}")
##print(createDirectory("resturant.txt", "directory.txt"))
"""
QT 4 
func name infectedPercentage()
take in country list and filename
Country1,Population,InfectedPopulation
"""
def infectedPercentage(countryList, filename):
    percentList = {}
    with open(filename) as file:
        reader = csv.reader(file)
        for country,cases, infected  in reader:
            try:
                percentList[country] = int(infected)/float(cases)
            except ValueError as e:
                continue
    max = float('-inf')
    bestCountry = ""
    for country in countryList:
        if percentList[country] > max:
            bestCountry = country
            max = percentList[country]
    max = round(max, 4) * 100
    result_Tuple = (bestCountry, max)
    return result_Tuple
##print(infectedPercentage(["Sweden", "Turkey", "Ukraine"],'infected.csv'))
"""
QT 5 
func name countryStatus()
take in country list and filename
return dictionary of keys for list of the country and 
value for risk level
low  <=25    <       medium  <= 65        <   high  <= 100
"""
def countryStatus(filename, countryList):
    statusDict = {}
    with open(filename) as file:
        reader = csv.reader(file)
        for country, cases, infected in reader:
            try:
                percent = float(infected)/float(cases)
                if percent <= .25:
                    statusDict[country] = "Low Risk"
                elif percent <=.65:
                    statusDict[country] = "Medium Risk"
                else:
                    statusDict[country] = "High Risk"
            except ValueError as e:
                continue
        result = {}
        for country in countryList:
            threatLevel = statusDict[country]
            if not threatLevel in result:
                result[threatLevel] = [country]
            else :
                list_threat = result[threatLevel]
                list_threat.append(country)
                result[threatLevel] = list_threat
        return result
##print(countryStatus("infected.csv", ["United States", "Tonga", "Poland", "New Zealand", "Norway"]))
"""
QT 6
funch name compareRisk()
take in country to compare, country list and filename
return country that have a smaller pop and larger infection pop than
input country
"""
def compareRisk(compareCountry, countryList, filename):
    countryDict = {}
    with open(filename) as file:
        reader = csv.reader(file)
        for country, pop, infected in reader:
            try:
                countryDict[country] = [float(pop), float(infected)]
            except ValueError as e:
                continue
        result = []
        population = countryDict[compareCountry][0]
        infection = countryDict[compareCountry][1]
        for country in countryList:
            pop = countryDict[country][0]
            infect = countryDict[country][1]
            if population > pop and infection < infect:
                result.append(country) 
        if len(result) == 0:
            return "No countries"
        return result
print(compareRisk("Tuvalu", ["Turkmenistan", "Norway", "Netherlands", "Philippines"], 'infected.csv'))


