str = input("Enter a character to check: ")
if str.isalpha():
    if str.lower() in 'aeiou':
        print(f"{str} is a vowel.")
    else:
        print(f"{str} is a consonant.")
else:
    print("Please enter a valid alphabetic character.")