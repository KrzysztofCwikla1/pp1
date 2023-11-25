def count_letter(text, letter):
    return text.count(letter)

# main program
text = "You never get a second chance to make a first impression"
letter_to_count = 'e'

result = count_letter(text, letter_to_count)
print(f"The number of letter '{letter_to_count}': {result}")