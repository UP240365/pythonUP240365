#1
count = 0
while count < 11:
    print(count)
    count = count + 1
print('-----')
numbers = [0, 1, 2, 3, 4, 5,6,7,8,9,10]
for number in numbers:
    print(number)
print('-----')
#2
count = 10
while count >= 0:
    print(count)
    count = count - 1
print('-----')
numbers = [10,9,8,7,6,5,4,3,2,1,0]
for number in numbers:
    print(number)
print('-----')
#3
for i in range(1, 8):
    print('#' * i)
print('-----')
#4
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()
print('-----')
#5
n=0
while n<=10:
    r= n*n
    print(n,'x',n,'=',r)
    n= n+1
print('-----')
#6
technologies = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for tech in technologies:
    print(tech)
print('-----')
#7
for number in range(0, 101):
    if number % 2 == 0:
        print(number)

print('-----')
#8
for number in range(0, 101):
    if number % 2 != 0:
        print(number)