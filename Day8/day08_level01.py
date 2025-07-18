#1
dog={}
#2
dog['Name']='Lucky'
dog['Color']='Black'
dog['Breed']='Aleman'
dog['Legs']='4'
dog['Age']='5'
print(dog)
#3
student = {
    "first_name": "John",
    "last_name": "Wesker",
    "gender": "Male",
    "age": 21,
    "marital_status": "Single",
    "skills": ["Python", "Data Analysis"],
    "country": "USA",
    "city": "New York",
    "address": "123 Main Street"
}
#4
print(len(student))
#5
print(student['skills'])
print(type(student['skills']))
#6
student['skills'].append('C++')
print(student)
#7
keys= student.keys()
print(keys)
#8
values= student.values()
print(values)
#9
tpl= student.items()
print(tpl)
#10
student.pop('gender')
#11
del student