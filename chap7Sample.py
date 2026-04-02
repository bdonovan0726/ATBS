#sazmple file demonstrating some dictionary usage

nameStr = 'Brian T. Donovan'
charCount = {}

for char in nameStr:
	charCount.setdefault(char, 0)
	charCount[char] += 1
	
for i in charCount.items():#dumps the keys and values
	print(i)
    
for x in charCount.keys():
    print(x + ': ' + str(charCount[x]))
    
for y,z in charCount.items():
    print('Key: ' + str(y) + '\nValue: ' + str(z) + '\n')
    
 ##unpacking tuples
smpTupList = [(1,2,3), (4,5,6), (7,8,9)]
for x,y,z in smpTupList:
    print(f'{x},{y},{z}')
 
for x, *rest in [(1, 2, 3), (4, 5, 6)]:
   print(x, rest)