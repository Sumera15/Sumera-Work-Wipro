'''Take a list of numbers as input and print the largest and smallest numbers in the list.
Take a string as input and print the length of the string.
Take a list of names as input and print the list in alphabetical order.
Take a list of numbers as input and print the total sum of the elements in the list.
Takes a string as input and print the string in uppercase. '''

#largest smallest in the list
num = [int(x) for x in input('Enter the numbers(space separated):').split()]
print("Largest number:", max(num))
print('Smallest number:', min(num))

#length of string
s = input('Enter a string:')
print('Length of string:', len(s))

#sort names
names = input('Enter names (space separated):').split()
print('Names in aplhabetical order:',sorted(names))

#sum of elements
num2 = list(map(int, input('Enter numbers for sum:').split()))
print('Total sum:', sum(num))

#string uppercase
s2 = input('Enter a string: ')
print('Uppercase string:',s2.upper())

