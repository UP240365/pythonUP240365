#1
score=int(input('Enter your final score:'))
if score >= 90 and score <= 100:
    print('Your final grade is A')
elif score >= 70 and score <= 89:
    print('Your final grade is B')
elif score >= 60 and score <= 69:
    print('Your final grade is C')
elif score >= 50 and score <= 59:
    print('Your final grade is D')
elif score >= 0 and score <= 49:
    print('Your final grade is F')
else:
    print('error')

#2
month=input('Enter a month:').capitalize()
if month in ["September", "October", "November"]:
    print('The season is Autumn')
elif month in ["December", "January", "February"]:
    print('The season is Winter')
elif month in ["March", "April", "May"]:
    print('The season is Spring')
elif month in ["June", "July", "August"]:
    print('The season is Summer')
else:
    print('error')

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit= input('Enter a fruit:')
if (fruit in fruits) == True:
    print('The fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)