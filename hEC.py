"""
QT 1
func name validParentheses()
take in list 
return true if parentheses are valid
"""
def validParentheses(line):
    stack = []
    for c in line:
        match c:
            case '[':
                stack.append(c)
            case '(':
                stack.append(c)
            case ']':
                if not len(stack) == 0:
                    top = stack.pop()
                if not top == '[':
                    return False
            case ')':
                if not len(stack) == 0:
                    top = stack.pop()
                if not top == '(':
                    return False
    if not len(stack) == 0:
        return False
    return True
##print(validParentheses("[3, 2, (1])"))
"""
QT 
func name take in list and length 
sort the list using bubble sort
"""
def bubbleSort(alist, length):
    if length == 0 or length == 1:
        return alist
    def sort(lp, rp):
        if rp >= length:
            return
        print(alist)
        print()
        if alist[lp] > alist[rp]:
            temp = alist[lp]
            alist[lp] = alist[rp]
            alist[rp] = temp
        if lp - 1 >= 0 and alist[lp] < alist[lp-1]:
            sort(lp-1, lp)
        else:
            sort(lp+1, rp+1)
    sort(0, 1)
    print(alist)
##print(bubbleSort([100,99,98,56,0], 5))
"""
QT 3
func name groupAnagrams()
take in list of string 
return dict of anagram and their different types 
"""
def groupAnagrams(strings):
    result = {}
    answer = {}
    for string in strings:
        add = False
        for c in string:
            prev = result.get(string, [])
            prev.append(c)
            result[string] = prev
        result[string].sort()
        if len(answer) == 0:
            answer[string] = [string]
        for key in result.keys():
            if key != string and result[key] == result[string]:
                prev = answer[key]
                prev.append(string)
                answer[key] = prev
                add = True
        if not add:
            answer[string] = [string]
    print(answer)
    return result
##print(groupAnagrams(['rat', 'act', 'stressed', 'desserts', 'cat']))
"""
QT 4 
implement freind class and planner class
"""
class Friend:
    def __init__(self, name:str, schedule:dict) -> None:
        self.name = name
        self.schedule = schedule
    def addActivity(self, activity:tuple):
        if not activity[0] in self.schedule:
            self.schedule[activity[0]] = activity[1]
        else:
            return "Not possible."
class Planner:
    def __init__(self, friendsList) -> None:
        self.friendsList = friendsList
    def freetime(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        rmv = []
        first = True
        for friend in self.friendsList:
            for day in friend.schedule:
                rmv.append(day)
        for day in rmv:
            if day in days:
                days.remove(day)
        if len(days) == 0:
            return "No one is free"
        return days
    def plans(self, day):
        map = {}
        for friend in self.friendsList:
            activity = friend.schedule[day]
            prev = map.get(activity, [])
            prev.append(friend.name)
            map[activity] = prev
