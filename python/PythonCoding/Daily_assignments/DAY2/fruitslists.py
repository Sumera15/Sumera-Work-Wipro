#list of fruits
print('List of fruits:')
fruits = ['mango','apple','grapes','banana','kiwi']
print(fruits)
#add two more fruits
print('After adding two fruits & removing one Fruits: ')
fruits.append('cherry')
fruits.append('orange')
fruits.remove('kiwi')
print(fruits)
#Acess 2nd and 4 th fruits
print('2nd fruit:', (fruits[2]))
print('4th fruit:', (fruits[4]))
#Slice the list to print 1st three fruits
print('First three Fruits: ')
print(fruits[0:3])
#Length of fruits
print('Length of Fruits:', (len(fruits)))
