#1
empty_tuple = ()
#2
brothers=('Miguel','Pepe')
sisters=('Julieta','Fabiola')
#3
siblings= brothers + sisters
#4
print(len(siblings))
#5
parents=('Fernando', 'Sandra')
family_members= siblings + sisters

#Level 2

#1
siblings= brothers + sisters
parents=('Fernando', 'Sandra')
#2
fruit=('Fresa','Durazno','Mango')
vegetables=('Zanahoria','Calabaza','Brocoli')
animal_products=('Hueso','Correa','Bozal')
food_stuff_tp= fruit+vegetables+animal_products
print(food_stuff_tp)
#3
food_stuff_lt= list(food_stuff_tp)
#4

#5
print(food_stuff_lt[3:6])
#6
del food_stuff_tp
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries) 
print('Iceland' in nordic_countries)