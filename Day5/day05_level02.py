
#1 sort
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
#min and max 
min=ages[0]
num=len(ages)-1
max=ages[num]
#add min and max
ages.insert(0,min)
num2=len(ages)-1
ages.insert(num2,max)
print(ages)
#median
mid1=ages[5]
mid2=ages[6]
median=(mid1+mid2)/2
print("The median age is: ", median)
#Average
total=len(ages)
sum=sum(ages)
avg=sum/total
print("The average age is: ", avg)
#range
range=max-min
print("The range is: ",range)
#compare
min_avg=abs(min-avg)
max_avg=abs(max-avg)
print("The value of min - average is ",min_avg)
print("And the value of max - average is",max_avg)
