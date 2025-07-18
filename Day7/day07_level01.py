# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#1
print(len(it_companies))
#2
it_companies.add('Twitter')
print(it_companies)
#3
it_companies.update(['Huawei','Instagram','Sony'])
print(it_companies)
#4
it_companies.remove('Google')
#5
"""
The discard() method removes the specified item from the set. 
This method is different from the remove() method, because the remove()
method will raise an error if the specified item does not exist, and the 
discard() method will not.
"""
