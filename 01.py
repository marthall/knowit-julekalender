
def is_palindrome(string): return string[::-1] == string
def to_octal(number): return str(oct(number))[1:]

# This is ugly and slow
# print len(filter(lambda i: is_palindrome(str(i)) and is_palindrome(to_octal(i)), range(1, 1000000)))

count = 0
for i in range(1, 1000000):
    if is_palindrome(str(i)) and is_palindrome(to_octal(i)):
        count += 1

print count
