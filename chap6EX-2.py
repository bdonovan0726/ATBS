import random
number_of_streaks = 0

resList = []
streakFlag= 0
lastchar = 'E'
currentStreak = 0
totalStreak100Set = 0
overallStreakCount = 0
targetStreakLength = 6

for x in range(100):
    if random.randint(0,1) == 0:
        resList[x] = 'H'
    else:
        resList[x] = 'T'
        
for x in range(100):#yes I know using the hardcoded 100 is badddd, but right now i dont care lol
    if resList[x] == lastchar:
        streakFlag = 1
        currentStreak += 1
    else:
        if currentStreak
        lastchar = resList[x]
        
        
for experiment_number in range(10000):  # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values

    # Code that checks if there is a streak of 6 heads or tails in a row

print('Chance of streak: %s%%' % (number_of_streaks / 100))