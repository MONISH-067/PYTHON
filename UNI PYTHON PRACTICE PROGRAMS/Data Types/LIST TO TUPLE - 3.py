list = []
x = int(input("Enter how many elements you want in list: "))
for _ in range(x):
    list.append(input("Enter the element: "))

print(f"The List is: {list}\nData Type before convertion : {type(list)}")
print(f"The Tuple is: {tuple(list)}\nData Type after convertion: {type(tuple(list))}")