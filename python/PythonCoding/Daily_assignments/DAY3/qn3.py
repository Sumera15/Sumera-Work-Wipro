def find_largest(n1, n2, n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

n1 = int(input('Enter first number:'))
n2 = int(input('Enter second number:'))
n3 = int(input('Enter third number:'))

largest = find_largest(n1, n2, n3)
print('Largest number is:', largest)