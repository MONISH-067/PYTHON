n = int(input("\nEnter a year: "))
print(f"\n{n} is a leap year.\n") if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0) else print(f"\n{n} is not a leap year.\n")