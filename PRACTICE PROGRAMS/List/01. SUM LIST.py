list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    list.append(element)
print("The sum of the elements in the list is:", sum(list))