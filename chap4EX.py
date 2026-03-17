def collatz(number):
	if number % 2 == 0:
		return number // 2
		
	else:
		return 3 * number + 1
		
print("Enter a number")
inNumber= input('Number:')
print('You entered:' + inNumber)

result = int(inNumber);
while result != 1:
    result = collatz(result)
    print(result)
print('Finished')
