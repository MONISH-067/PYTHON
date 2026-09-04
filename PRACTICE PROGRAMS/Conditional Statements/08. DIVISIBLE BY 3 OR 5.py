n = int(input("Enter a number to check: "))
if n % 3 == 0 and n % 5 == 0:
    print(f"{n} is divisible by both 3 and 5.")
elif n % 3 == 0:
    print(f"{n} is divisible by 3 but not by 5.")
elif n % 5 == 0:
    print(f"{n} is divisible by 5 but not by 3.")
else:
    print(f"{n} is not divisible by both 3 and 5.")