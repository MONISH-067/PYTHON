n = int(input("\nEnter a number: "))
print(f"\n{n} is a negative number.\n") if n < 0 else print(f"\nThe number {n} is zero.\n") if n == 0 else print(f"\n{n} is a positive number.\n")