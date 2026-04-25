
#function def
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

#taking input
num = int(input('Enter a positive number:'))

#Calling function and printing result

result = factorial(num)
print('Factorial of', num,'is:', result)