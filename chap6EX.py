import random

gearlistt = ['BC', 'Regs', 'Mask', 'Fins', 'Tank', 'Computer', 'Boots']

def printlistt(list):
    retString = ''
    if len(list) == 0:
        return None;
    else:
        for i in range(len(list) - 1):
            retString += list[i] + ', '
        retString += 'and ' + list[len(list)-1]
        return retString

print(printlistt(gearlistt))