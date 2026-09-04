str = input("\nEnter anything: ")
print(f"{str} contains only digits" if str.isdigit() else f"{str} contains other characters")