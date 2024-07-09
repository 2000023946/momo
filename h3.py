"""
QT 1
func name movieNight()
takes in a caption 
return a string without numbers
"""
def movieNight(caption):
    result = ""
    for i, c in enumerate(caption):
        if not c.isdigit():
            result += c
    return result
##print(movieNight("Mr. and M4rs. Dursley of nu28mber four, Privet Drive, wer903e proud to say th6at they we6re perfectly norm3al, tha894nk you ve89ry much."))
"""
QT 2
func name iceCream()
take in ice creame flavor and num of vowels
you have only ahve a flavor with x num of vowels
return yes, {flavor} ice cream has nmore than {number} vowels!
no {flavor} ice cream doesn't have morethan {number} vowels!
"""
def iceCream(flavor, number):
    vowels = 0;
    for c in flavor:
        if c in 'aeiou':
            vowels +=1
    if vowels > number:
        return f"Yes, {flavor} ice cream has more than {number} vowels!"
    return f"No, {flavor} ice cream has more than {number} vowels!"
##print(iceCream("Vanilla", 2))
"""
QT 3
func name dreamCar()
take in a price of car, bank balance, interest rate
return how mnay years your savings account will have price of car
"""
def dreamCar(price, balance, rate):
    rate  = (rate*0.01) + 1
    years = 0
    while balance < price:
        balance *= rate
        years +=1
    return years
##print(dreamCar(100000, 112.15, 2.1))
"""
QT 4
func name battleship()
take in a board size for battle ship
print out the board
"""
import string
def battleship(size):
    alphabet = string.ascii_lowercase
    print(alphabet[0:size])
    for l in alphabet[0:size]:
        for x in range(1, size+1):
            print(f"{l}{x} ", end="")
        print()
##battleship(6)
"""
QT 5
func name tennisMath()
take in player 1 and player 2, and set of 1 and 2, - means new game
1 is poin for p1 and 2 is point for p2
return winnre of match and score 
it tie say it is tie
"""
def tennisMatch(player1, player2, record):
    score1, score2 = 0, 0
    point1, point2 = 0, 0
    for n in record:
        if n.isdigit():
            if n == '1': point1 +=1
            else: point2 +=1
        else:
            if point1 > point2: score1 +=1
            elif point1 < point2: score2 +=1
            point1, point2 = 0, 0
    if score1 > score2:
        return f"{player1} won! The score was {score1}-{score2}"
    elif score1 < score2:
        return f"{player2} won! The score was {score2}-{score1}"
    return "It's a tie!"
##print(tennisMatch("Arvin", "Arushi", "1122-22211-11122-1212-"))


