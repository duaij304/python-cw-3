#الجزء الاول 

favorite_animals = ['lion', 'cat', 'monkey', 'rabbit']

print(favorite_animals)

print(favorite_animals[1])

favorite_animals.remove("monkey")
print(favorite_animals)
#الجزء الثاني

favorite_animals.append('camel')

for animal in favorite_animals:
    print("I love  " + animal)

numbers = [1, 2, 3, 4, 5]
numbers_sum = 0
#الجزء الثالث 
for number in numbers:
    numbers_sum += number
print("Total :", numbers_sum)
