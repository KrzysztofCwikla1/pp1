def separate_characters(text):
    return '-'.join(text)

# main program
text1 = "University"
text2 = "UE"
text3 = "x"
text4 = ""

print(f"f(\"{text1}\") returns \"{separate_characters(text1)}\"")  # "U-n-i-v-e-r-s-i-t-y"
print(f"f(\"{text2}\") returns \"{separate_characters(text2)}\"")  # "U-E"
print(f"f(\"{text3}\") returns \"{separate_characters(text3)}\"")  # "x"
print(f"f(\"{text4}\") returns \"{separate_characters(text4)}\"")  # ""