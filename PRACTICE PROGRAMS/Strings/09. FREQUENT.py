str = input("\nEnter any sentence: ")
c, max, index = 0, 0, 0
for i in str.split():
    if len(i) > max:
        max = len(i)
        index = c
    c += 1
print(f"Most frequent word: {str.split()[index]}")