def is_palindrome(s):
    return s == s[::-1]

word = input('Enter a string:')
result = is_palindrome(word)
print('Is Palindrome:', result)