def collatz(number):
	if number % 2 == 0:
		return number // 2
		
	else:
		return 3 * number + 1
		
while True:
    try:
        print('Enter a number')
        inNumber = input('Number:')
        result = int(inNumber)
        break
    except ValueError:
        print('Enter a number only please')
        continue

while result != 1:
    result = collatz(result)
    print(result)
        
print('Finished')