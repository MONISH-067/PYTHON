x, y = int(input("Enter from: ")), int(input("Enter to: "))
print("Prime numbers between", x, "and", y, "are:")
for num in range(x, y + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)