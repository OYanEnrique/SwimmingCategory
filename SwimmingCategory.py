#Swimming Category

age=int(input('Enter your age:\n'))

if age<=9:
	print('Your Category is: Age group 9-10 years')
elif age <= 14:
	print('Your Category is: Age group 11-14 years')
elif age <= 19:
	print('Your Category is: Junior')
elif age <= 20:
	print('Your Category is: Senior')
else:
	print('Your Category is: Master')