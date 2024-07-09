"""
QT 1
func name findMax()
take in a lsit, start index, and end index(indclusive)
returns highest number
"""
def findMax(list, start, end):
    max = float('-inf')
    for n in list[start: end +1]:
        if n > max:
            max = n
    return max
##print(findMax([1, 8, 3, 2, -4], 2, 4))
"""
QT 2
func name fruitPie()
take in list of fruits, minimum quantity 
[f1, q1, f2, q2,...fn, qn]
return the fruits who have a greater quantity than the min
"""
def fruitPie(list, min):
    result = []
    prev = ""
    for i, item in enumerate(list):
        if i % 2 == 0:
            prev = item
        else:
            if item > min:
                result.append(prev)
    return result
##print(fruitPie(["peach", 55, "orange", 32, "pineapple", 2], 50))
"""
QT 3
func name replace word
take in initial sentence, replacement word
return corrected sentence
every word with length of 5 or greater is replaced 
"""
def replaceWord(sentence, replacement):
    result = ""
    sentence = sentence.split()
    for word in sentence:
        if len(word) >= 5:
            result += replacement
        else:
            result += word
        result += " "
    return result
##print(replaceWord('I missed the old Kanye', 'coding'))
"""
QT 4
func name highest sum
takes in a list of string
calc the sum of each string 
return the index of the highest sum in the list of string
"""
def highestSum(list):
    max = 0
    index = -1
    for i, string in enumerate(list):
        sum = 0
        for c in string:
            if c.isdigit():
                sum += int(c)
        if sum > max:
            max = sum
            index = i
    return index
##print(highestSum(["py1h0n", "1s", "v3ry", "fun!!11!!!111"]))
"""
QT 5
func name sublist
take in listA, listB
return true is listB is a sublist of listA
all elements of B are in same order as appeared in listA
"""
def sublist(listA, listB):
    if len(listB) == 0:
        return True
    ap = 0
    bp = 0
    while listA[ap] != listB[bp]:
        ap += 1
    while(bp < len(listB)):
        if listA[ap] != listB[bp]:
            return False
        ap+= 1
        bp += 1
    return True
##print(sublist(['a', 'b', 'd', 'e', 't'], ['b', 'd', 'e']))

