#1
empty_list= list()
#2
list=['banana', 'orange', 'mango', 'lemon', 'apple']
#3
print(len(list))
#4
print(list[0])
print(list[2])
print(list[4])
#5
mixed_data_types=['Luis', '19', '1.83', 'single', 'nublado']
#6
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7
print(it_companies)
#8
print(len(it_companies))
#9
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])
#10
it_companies[0]='Instagram'
print(it_companies)
#11
it_companies.append('Samnsung')
print(it_companies)
#12
it_companies.insert(4,'Cisco')
print(it_companies)
#13
it_companies[1] = it_companies[1].upper()
print(it_companies)
#14
it='# '.join(it_companies)
print(it)
#15
print('Microsoft' in it_companies)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.sort(reverse=True)
print(it_companies)
#18
print(it_companies[2:])
#19
print(it_companies[0:6])
#20
mid=len(it_companies)//2
print(it_companies[:mid]+it_companies[mid+1:])
#21
it_companies.pop(0)
print(it_companies)
#22
it_companies.pop(3 and 4)
print(it_companies)
#23
last=len(it_companies)-1
it_companies.pop(last)
#24
it_companies.clear()
print(it_companies)
#25
del it_companies
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
all=front_end + back_end
print(all)
#27
full_stack=all


