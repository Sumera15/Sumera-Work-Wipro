
#Count how many times "a" appears using enumerate

s = input('Enter a string:')
count = 0

for index, char in enumerate(s):
    if char == 'a':
        count += 1

print('Count of "a" :', count)
