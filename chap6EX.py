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

neededGear= printlistt(gearlistt)
if neededGear == None:
    print('Empty list, exiting')
else:
    print('To execute a SCUBA dive prooperly you need ' + neededGear)