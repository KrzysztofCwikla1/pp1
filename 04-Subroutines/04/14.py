def remove_spaces(sentence):
    return sentence.replace(" ", "")

# main program
sentence1 = "integrated development environment"
sentence2 = "A programming language is a system of notation for writing computer programs"

print(f"f(\"{sentence1}\") returns \"{remove_spaces(sentence1)}\"")  # "integrateddevelopmentenvironment"
print(f"f(\"{sentence2}\") returns \"{remove_spaces(sentence2)}\"")  # "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms"