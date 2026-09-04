n = int(input("Enter a number to check: "))
if n < 0:
    print(f"{n} is negative.")
elif n == 0:
    print(f"{n} is zero.")
else:
    print(f"{n} is positive.")