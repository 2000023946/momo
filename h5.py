"""
QT 1 
func name showToWatch()
take in friendsFavShows and yours 
return friends who have same fav show as you. in alpabetical order
"""
def showToWatch(friendsFav, yourFav):
    result = []
    friend = ""
    for element in friendsFav:
        for i,item in enumerate(element):
            if i % 2 == 0:
                friend = item
            else:
                for show in item:
                    if yourFav == show:
                        result.append(friend)
                        break
    if len(result) == 0:
        return "Lonley Night :("
    result.sort()
    return result
##print(showToWatch([('Maria', ['Euphoria']),('Romy', ['Gilmore Girls']),('Lynn', ['You', 'Gossip Girl'])], 'Euphoria'))
"""
QT 2
func name fixLabels()
take in list of labels 
return fixed one, 1st number -> 1st string and nth number -> nth string
"""
def fixLabels(labelList):
    result = []
    numPointer = 0
    stringPointer = 0
    while isinstance(labelList[stringPointer], float):
        stringPointer += 1
    while isinstance(labelList[numPointer], str):
        numPointer += 1
    while stringPointer < len(labelList) and numPointer < len(labelList):
        if isinstance(labelList[stringPointer], str) and isinstance(labelList[numPointer], float):
            newTuple = (labelList[stringPointer], labelList[numPointer])
            result.append(newTuple)
        stringPointer +=1
        numPointer +=1
        while stringPointer < len(labelList) and isinstance(labelList[stringPointer], float):
            stringPointer += 1
        while numPointer < len(labelList) and isinstance(labelList[numPointer], str):
            numPointer += 1
    result.sort()
    return result
##print(fixLabels([2.99, 5.49, 'chocolate', 1.99, 'ice cream', 'candy']))
"""
QT 3
func name playList()
take in playlist of song
return tuple of all of the songs and time to listne to all of it
"""
def newPlaylist(playlist):
    songList = []
    time = 0
    for list_tuple in playlist:
        for i, element in enumerate(list_tuple):
            if i % 2 == 0:
                songList.append(element)
            else:
                min, sec = "", ""
                m, s = True, False
                for digit in element:
                    if digit == ':':
                        m = not m
                        s = not s
                        continue
                    if m:
                        min += digit
                    if s:
                        sec += digit
                time  = time + float(min) + (float(sec)/60)
    songList.sort()
    tupleList = (songList)
    result = [tupleList, time]
    return result
##print(newPlaylist([("All Too Well", "10:13"),("Forever & Always", "3:46"),("Love Story", "3:56"),("Mr. Perfectly Fine", "4:38")]))
"""
QT 4 
func name birthdays()
take in list of friends and birthdates list
return birthdays who fall on weekend
"""
import datetime
def birthdays(friends, Bdays):
    result = []
    pF, pB = 0, 0
    while pF < len(friends) and pB < len(Bdays):
        date = datetime.date(2022, Bdays[pB][0], Bdays[pB][1])
        day = date.weekday()
        if day == 5 or  day == 6:
            result.append(friends[pF])
        pF +=1
        pB +=1
    result.sort()
    return result
##print(birthdays(['Audrey', 'Paige', 'Anastasia', 'Ramya', 'Lasya', 'Cynthia'], [(5,6), (4,7), (1,19), (12,4), (9,10), (3,6)]))
"""
QT 5
func name smashBros()
take in list of figher for smash, and opponent 
return list of counter for opponent
if none return no counters !
"""
def smashBros():
    



            