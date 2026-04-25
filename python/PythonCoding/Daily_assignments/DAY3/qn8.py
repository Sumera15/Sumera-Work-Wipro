import random
#1
random_integer = random.randint(1,100)
print('Random integer between 1 and 100:', random_integer)
#2
random_list = []

for i in range(10):
    random_list.append(random.randint(1,100))

print('List of random numbers:', random_list)

#3
numbers = [1,2,3,4,5,7,6,8,7]
random.shuffle(numbers)

print('Shuffled list:', numbers)