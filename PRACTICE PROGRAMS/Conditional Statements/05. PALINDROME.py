str = input("\nEnter a string: ")
print(f"\n'{str}' is a palindrome.\n") if str.lower() == str.lower()[::-1] else print(f"\n'{str}' is not a palindrome.\n")