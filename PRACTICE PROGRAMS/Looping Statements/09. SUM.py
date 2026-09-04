x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
i = x
sum = 0
while x <= y:
    sum += x
    x += 1
print("The sum of numbers from", i , "to", y, "is:", sum)