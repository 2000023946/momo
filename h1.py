## QT 1
##listen function :
##asks the user how manu songs and podcasts they listen to 
##print responce how much time they spend lsitening to songs and podcasts
##song is 3 min             Podcast is 25
def listen():
    x = input("How many songs did you listen to? ")
    y = input("How many podcasts did you listen to? ")
    time = 3*int(x) + 25*int(y)
    minutes = time % 60
    hours = int((time - minutes)/60)
    int(hours)
    print("By listening to " + str(x) + " songs and " + str(y) + " podcasts, you have spent "+ str(hours)+" hours and "+str(minutes) +" minutes on Spotify")
"""
QT 2
DOMINO's TIME
function name dominostime
print responce saying x pizzas, and y pasta and z chiceken wings
is $______. 
pizza -> 12          pasta -> 6         chicken wings -> 8
"""
def dominosTime():
    x = input("How many pizzas do you want? ")
    y = input("How many pastas do you want? ")
    z = input("How many chicken wings do you want? ")
    total = 12*int(x) + 6*int(y) + 8*int(z)
    print("By ordering "+x+" pizzas, "+y+ " orders of pasta, and "+z+" orders of chicken wings, your order total comes to $"+str(total)+".")
"""
QT 3
funciton name tipAndSplit()
take an order total, percentage of tip, and how many pple to split
print tip the dirver gets and how much each person pays
"""
def tipAndSplit():
    x = input("What was the order total? ")
    y = input("What percentage would you like to tip? ")
    z = input("How many people are splitting the order? ")
    tip = int(x) * 0.01*int(y)
    tip = round(tip, 2)
    share = (int(x)+tip)/int(z)
    share = round(share, 2)
    print("The driver got a tip of $"+str(tip)+". Each person paid $"+str(share)+".")
"""
QT 4
function name youtuber()
take in num of vidoes made, money made per view, num of view 
print " You have made x by makign YouTube videos!
"""
def youtuber():
    x = input("How many videos have you made? ")
    y = input("How much do you get paid per view? ")
    z = input("How many views do your videos have? ")
    moneyMade = int(x) * float(y) * int(z)
    moneyMade = round(moneyMade, 2)
    print("You have made $"+str(moneyMade)+" by making YouTube videos!")
youtuber()
"""
QT 5
function name bathBomb()
take in a radius for input
print: the volume of a bath bomb with a radius r, is Volume
"""
def bathBomb():
    x = input("What is the radius of the bath bomb? ")
    v = (4/3)*(3.14)*(pow(int(x), 3))
    v = round(v, 2)
    print("The volume of a bath bomb with a radius "+x+" is "+str(v)+".")
bathBomb()