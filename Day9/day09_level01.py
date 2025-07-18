#1
age=int(input('Enter your age:'))
if age >= 18:
    print('You are old enough to drive')
else:
    a= 18-age
    print('You need',a,'years to drive')

#2
my_age=19
your_age= int(input('Enter your age:'))

if your_age > my_age:
    a=your_age-my_age
    print('You are',a,'years older than me')
elif your_age < my_age:
    a=my_age-your_age
    print('I am',a,'years older than you')
elif your_age == my_age:
    print('We have the same age')

#3
a=int(input('Enter number one:'))
b=int(input('Enter number two:'))

if a > b:
    print(a,'is greater than',b)
elif a < b:
    print(a,'is smaller than',b)
else:
    print(a,'is equal to',b)