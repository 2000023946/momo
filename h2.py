"""
QT 1 
function name skillLevel()
takes in number 
returns beginner if num <25, moderate [25, 75], and advaned >75
"""
def skillLevel(passRate):
    if passRate < 25:
        return 'Beginner'
    elif passRate < 75:
        return 'Moderate'
    return 'Advaceed'
##print(skillLevel(80))
"""
QT 2
fun name bookStore()
takes in item you want to buy, amount of money you have, and quantity 
you are going to buy
shirt : 15.50,     laynard : 4.25,     sweatshirt : 25, mug : 10.5
money left over in 2 decimal, if not enough return not enour money
"""
def bookStore(item, walletAmount, quantity):
    items  = {
        'Shirt' : 15.50,
        'Lanyard' : 4.25,
        'Sweatshirt' : 25,
        'Mug' : 10.50
    }
    if item in items:
        price = items.get(item)
    amount = price * quantity
    moneyLeftOver = walletAmount - amount
    if moneyLeftOver < 0:
        return 'Not enough money!'
    return round(moneyLeftOver, 2)
##print(bookStore('Shirt', 300.5, 10))
"""
QT 3
func name dinnerPlans()
take in distance and hunger level
return decision to take either uber or walk to resturant
"""
def dinnerPlans(distance, hungerLevel):
    map = {
        'Not Hungry' : 7,
        'Slightly Hungry' : 5,
        'Hungry' : 3,
        'Very Hungry' : 1
    }
    hl = map.get(hungerLevel)
    if distance > hl:
        return 'Uber'
    return 'Walk'
##print(dinnerPlans(.5, 'Very Hungry'))
"""
QT 4 
func name weekendTrip()
take in distance, speed, freetime
if travel time is < 20 % of freetime return mode of transport:
speed - > [2.5, 15] walking
(15, 20] -> biking
speed [20, infi] - > driving
else return going to this diest would take too much time
"""
def weekendTrip(distance, speed, freeTime):
    time = distance/speed
    if time < freeTime*.2:
        if 2.5 <= speed <=15:
            return 'Walking'
        elif 15 < speed <= 20:
            return 'biking'
        return 'driving'
    return 'Going to this destination would take too much time'
print(weekendTrip(10, 5, 8))
"""
QT 
func name textFriends()
take in distance, speed ,freetime, numSnakcs, numFriends
return textMsg
if trip is 20 % or less of your free time return 
if each of us gets ___snacks there will be ___left. i will be ___, 
who else is doing the same?
"""
def textFriends(distance, speed, freeTime, numSnacks, numFriends):
    decision = weekendTrip(distance, speed, freeTime)
    if(decision == 'Going to this destination would take too much time'):
        return decision
    left = numSnacks % numFriends
    snacks = (numSnacks) //numFriends
    textMsg = f'If each of us gets {snacks} snack(s), there will be {left} left. I will be {decision} who else is doing the same?'
    return textMsg
print(textFriends(25, 65, 2.5, 13, 7))

