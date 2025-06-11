import math 
#1-3
age=(18)
altura=(1.83)
complex_number=(6 + 3j)
#4
base=int(input("Ingrese la base del triangulo:"))
height=int(input("Ingrese la altura del triangulo:"))
print("Area:")
print(0.5*base*height)
#5
a=int(input("Ingrese el lado A del triangulo:"))
b=int(input("Ingrese el lado B del triangulo:"))
c=int(input("Ingrese el lado C del triangulo:"))
print("Perimetro:")
print(a+b+c)
#6
length=int(input("Ingrese la longitud del rectangulo:"))
width=int(input("Ingrese el ancho del rectangulo:"))
area=(length*width)
perimeter=(2*(length+width))
print("Area:", area)
print("Perimetro:", perimeter)
#7
radius=int(input("Ingrese el radio del circulo:"))
pi=3.1416
area_circle=(pi*radius**2)
circumference=(2*pi*radius)
print("Area:", area_circle)
print("Circunferencia:", circumference)
#8 y = 2x - 2
slope=2
y_intercept=-2
x_intercept=1
#9
x1, y1 = 2, 2
x2, y2 = 6, 10
slope2 = ((y2 - y1)/(x2 - x1))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#10
print(slope==slope2)
#11 y=x**2 + 6x + 9
x=-3
y=(x**2 + 6*x +9)
print(y)
#12
py=len('python')
dr=len('dragon')
print(py == dr)
#13
on=("on" in "dragon" and "on" in "python")
print("Is 'on' in both 'python' and 'dragon'?", on)
#14
jargon=("jargon" in "I hope this course is not full of jargon")
print("Is 'jargon' in the sentence 'I hope this course is not full of jargon'?", jargon)
#15
ont=('on' not in 'dragon' and 'on' not in 'python')
print("There is no 'on' in both dragon and python", ont)
#16
length_python = len('python')
print(float(length_python))
print(str(length_python))
#17
number = int(input("Ingrese un numero par:"))
par=(number % 2 == 0)
print("Su numero es par:", par)
#18
floor=(7 // 3 == int(2.7))
print("the floor division of 7 by 3 is equal to the int converted value of 2.7.", floor)
#19
type=(type('10') == type(10))
print("type of '10' is equal to type of 10", type)
#20
l=(int(float('9.8')) == 10)
print("int('9.8') is equal to 10", l)
#21
hours=int(input("Enter hours:"))
pay=int(input("Enter rate per hours:"))
print("Your weekly earning is", hours*pay)
#22
years = int(input("Enter numer of years you have lived:"))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")
#23
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")