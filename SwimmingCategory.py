#Swimming Category

age=int(input('Enter your age:\n'))

if age<=9:
	print('Your Category is: Child')
elif age <= 14:
	print('Your Category is: Youth')
elif age <= 19:
	print('Your Category is: Junior')
elif age <= 20:
	print('Your Category is: Senior')
else:
	print('Your Category is: Master')