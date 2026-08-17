def area(b, h):
    return (b * h)/2

b, h = map(int, input("\nEnter base and height of the triangle with space: ").split())
print(f"The area of triangle of base {b} and height {h} is {area(b, h)}\n")