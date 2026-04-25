from stringoperations import reverse_string, to_uppercase, string_length
from stringvalid import is_alpha, is_palindrome

from Daily_assignments.DAY3.qn6 import is_palindrome

text = "madam"
print('Original:', text)
print('Reversed:', reverse_string(text))
print('Uppercase:', to_uppercase(text))
print('Length:', string_length(text))

print('Is Palindrome:', is_palindrome(text))
print('Is Alphabet Only:', is_alpha(text))