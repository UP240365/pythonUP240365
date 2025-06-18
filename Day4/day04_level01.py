#1
thirty="Thirty "
days="Days "
of="Of "
python="Python"
sentence=thirty + days + of + python
print(sentence)
#2
coding="Coding "
forr="For "
all="All"
sentence2=coding + forr + all
print(sentence2)
#3
company="Coding For All"
#4
print(company)
#5
print(len(company))
#6
print(company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
slice = company[6:]
print(slice)
#10
print(company.find('Coding'))
#11
print(company.replace('Coding', 'Python'))
#12
f="Python For Everyone"
print(f.replace('Everyone', 'All'))
#13
print(company.split())
#14
s="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(s.split(', '))
#15
print(company[0])
#16
last= len(company) -1
print(company[last])
#17
print(company[10])
#18
f1=f[0]
f2=f[7]
f3=f[11]
acr= f1 + f2 +f3
print(acr)
#19
c1=company[0]
c2=company[7]
c3=company[11]
acr2= c1 + c2 +c3
print(acr2)
#20
print(company.find("C"))
#21
print(company.find("F"))
#22
comp= "Coding For All People"
print(comp.find("l"))
#23
sent="You cannot end a sentence with because because because is a conjunction"
print(sent.find("because"))
#24
print(sent.rfind("because"))
#25
slice2= sent[0:31]
slice3= sent[55:]
print(slice2+slice3)
#26 es igual al 23
#27 es igual al 25
#28
print(company.startswith("Coding"))
#29
print(company.endswith("coding"))
#30
strip='   Coding For All      '
print(strip.strip(' '))
#31
k = '30DaysOfPython'
print(k.isidentifier())
k2 = 'thirty_days_of_python'
print(k2.isidentifier()) 
#32
n=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(n)
print(result)
#33
print("I am enjoying this challenge. \nI just wonder what is next.")
#34
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")
#35
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print(formated_string)
#36
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')