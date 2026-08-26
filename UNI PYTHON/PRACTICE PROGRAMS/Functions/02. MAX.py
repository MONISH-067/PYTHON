def max(a , b, c):
    max = a
    if b > max and b > c:
        max = b
    elif c > max and c > b:
        max = c
    return max

a, b, c = map(int, input("\nEnter three numbers separated by space to find the maximum: ").split())
print(f"\nThe max value among {a}, {b} and {c} is {max(a, b, c)}\n")