#sazmple file demonstrating some dictionary usage

nameStr = 'Brian T. Donovan'
charCount = {}

for char in nameStr:
	charCount.setdefault(char, 0)
	charCount[char] += 1
	
for i in charCount.items():#dumps the indexes and values
	print(i)
    
for x in charCount.keys():
    print(x + ': ' + str(charCount[x]))
    
for y,z in charCount.items():
    print('Key: ' + str(y) + '\nValue: ' + str(z) + '\n')