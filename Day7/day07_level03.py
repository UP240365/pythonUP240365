#1
age = [22, 19, 24, 25, 26, 24, 25, 24]
setage= set(age)
print(len(age))
print(len(setage))
#the list is bigger
#2
"""
En Python, un String es una secuencia de caracteres que se utiliza para 
almacenar texto y es inmutable, lo que significa que no se puede modificar 
una vez creada. Una lista es una colección ordenada y mutable que puede 
contener elementos de cualquier tipo y admite duplicados, lo que la hace 
útil para almacenar y modificar secuencias de datos. Una tupla es similar 
a una lista en que está ordenada y puede contener múltiples tipos de datos, 
pero es inmutable; por lo tanto, una vez creada, su contenido no se puede 
modificar. Un set, por otro lado, es una colección desordenada de 
elementos únicos, lo que significa que no admite duplicados ni mantiene el 
orden de los elementos; se utiliza principalmente para realizar pruebas de 
pertenencia y eliminar entradas duplicadas.
"""
#3
sentence="I am a teacher and I love to inspire and teach people"
words = sentence.split()
print(words)
unique=set(words)
print(unique)