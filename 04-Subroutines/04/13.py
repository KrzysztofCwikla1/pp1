def is_palindrome(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalpha() or char.isdigit())
    return cleaned_string == cleaned_string[::-1]

# main program
palindrome1 = "radar"
palindrome2 = "12-11-21"
non_palindrome = "book"

print(f"f(\"{palindrome1}\") returns {is_palindrome(palindrome1)}")  # True
print(f"f(\"{palindrome2}\") returns {is_palindrome(palindrome2)}")  # True
print(f"f(\"{non_palindrome}\") returns {is_palindrome(non_palindrome)}")  # False