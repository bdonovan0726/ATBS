def collatz(number):
	if number % 2 == 0:
		return number // 2
		
	else:
		return 3 * number + 1
        
print('Enter a number')		
while True:
    try:
        inNumber = input('Number:')
        result = int(inNumber)
        break
    except ValueError:
        print('Enter a number only please')
        continue

while result != 1:
    result = collatz(result)
    print(result, sep=" ", end=" ")

print()        
print('Finished')