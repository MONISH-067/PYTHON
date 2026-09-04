n = int(input(  "Enter a number to check: "))
if n < 0:
    print("Enter a valid positive number.")
elif n == 0:
    print(f"{n} is neither even nor odd")
elif n % 2 == 0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")