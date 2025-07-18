import random
#1
def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled
print("La shuffled list es:", shuffle_list([1, 2, 3, 4, 5]))

#2
def unique_random_numbers():
    return random.sample(range(10), 7)
print("Los numeros random en un rango de 0-9 es:", unique_random_numbers())
