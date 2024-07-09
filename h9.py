"""
QT 1
func name pickyEater()
take in list of food
return number of even charactered items in the string
"""
def pickyEater(foodList):
    def traverse(index, count):
        if index >= len(foodList):
            return count
        food = foodList[index]
        if len(food) % 2 == 0 and not len(food) == 0:
            count +=1
        return traverse(index + 1, count)
    return traverse(0, 0)
##print(pickyEater(["Apple Pie", "Turkey", "Cranberry Sauce", "Mac and cheese"]))
"""
QT 2
func name inviteFriends()
take in a nested list
return a flattened list
"""
def inviteFriends(nestedList):
    result = []
    def traverse(element):
        if isinstance(element, str):
            result.append(element)
            return
        def travel(element, index):
            if index >= len(element):
                return
            traverse(element[index])
            travel(element, index +1)
        travel(element, 0)
    def travelLoop(index):
        if index >= len(nestedList):
            return
        traverse(nestedList[index])
        travelLoop(index+1)
    travelLoop(0)
    return result
"""print(inviteFriends([
'Parul',
'Megan',
['Arvin', 'Anthony', 'Arushi', ['Jasmine', 'Josh', 'Yara']]
]))"""
"""
QT 3 
func name friendsgiving()
take in list of tuples stores, budget, maxDistance
return a dict that has key_store and value_price 
the stores in the dict should be less than the max distance 
and less than the budget
"""
def friendsgiving(stores, budget, maxDistance):
    dict = {}
    def traverse(element, index, store, price, distance):
        if len(store) > 0 and price > 0 and distance:
            dict[store] = price
            return
        if index >= len(element):
            return 
        if isinstance(element[index], str):
            store = element[index]
        elif isinstance(element[index], float) and element[index] < budget:
            price = element[index]
        elif isinstance(element[index], int) and element[index] < maxDistance:
            distance = True
        traverse(element, index + 1, store, price, distance)
    def travel(index):
        if index >= len(stores):
            return
        traverse(stores[index], 0, "", -1, False)
        travel(index +1)
    travel(0)
    return dict
"""print(friendsgiving([('Sprouts', 3.45, 2),
('ALDI', 3.69, 6),
('Walgreens', 1.99, 1),
('Kroger', 2.79, 4)], 3.5, 5))"""
"""
QT 4 
func name palindrome()
take in string and and guess for how mnay 3 letter palindrome are in the str
return true if you are right and false if you are wrong
"""
def palindrome(word, guess):
    def traverse(i):
        if i >= len(word):
            return 0
        if i -1 > 0 and i+2 <= len(word) and isPali(word[  i-1  :  i+2  :  1   ]):
            return traverse(i+1) + 1 
        return traverse(i+1)
    num = traverse(0)
    if guess == num:
        return True
    return False
def isPali(word):
    if len(word) <= 1:
        return True
    if word[0] == word[len(word) -1]:
        return isPali(word[ 1 : len(word) -2 :  1  ])
    return False
print(palindrome("cdecec", 3))
    

