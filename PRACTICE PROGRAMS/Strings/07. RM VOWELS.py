str = input("\nEnter any word: ")
rm_vowels = ''.join([char for char in str if char.lower() not in 'aeiou'])
print(f"String after removing vowels: {rm_vowels}\n")