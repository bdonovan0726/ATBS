import random
import sys
import argparse

parser =argparse.ArgumentParser(description='Example parser')

parser.add_argument(
    "-r", "--runcount",
    required = True,
    type= int,
    help="Number of runs to execute"
)

parser.add_argument(
    "-s", "--streak",
    default = 6,
    type = int,
    help="Streak size"
)
  
args = parser.parse_args()

number_of_streaks = 0
lastchar = 'E'
currentStreak = 0
overallStreakCount = 0
targetStreakLength = args.streak
runCounter = 0

while runCounter < args.runcount:
    resList = []
    for x in range(100):
        if random.randint(0,1) == 0:
            resList.append('H')
        else:
            resList.append('T')
            
    runStreakCount = 0       
    for x in range(100):#yes I know using the hardcoded 100 is badddd, but right now i dont care lol
        if resList[x] == lastchar:
            currentStreak += 1
        else:
            if currentStreak == targetStreakLength:#condition to end our streak counting
                runStreakCount += 1
                print(f"Added a streak of {resList[x]}")

            currentStreak = 1          
            lastchar = resList[x]
            
    print(f'I found {runStreakCount} total streaks in this run')
    overallStreakCount += runStreakCount
    runCounter += 1
    lastchar = 'E'

print(f'Overall streak count is {overallStreakCount}')
