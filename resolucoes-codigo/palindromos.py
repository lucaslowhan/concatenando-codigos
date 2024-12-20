def is_palindrome(s):
    s = ''.join(s.split()).lower()
    return s == s[::-1]

test_string = "A man a plan a canal Panama"
print(f"'{test_string}' is a palindrome: {is_palindrome(test_string)}")