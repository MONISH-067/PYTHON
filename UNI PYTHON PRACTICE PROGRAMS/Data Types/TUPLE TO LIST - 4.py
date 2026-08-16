tuple = ("tuple", 67, 3.14, True, ["list"], {"set"}, {"dict" : "Dictionary"})
list = list(tuple)
print(f"\nThe Tuple is: {tuple}\nData Type before conversion: {type(tuple)}")
print(f"\nData Type after conversion: {type(list)}\nThe List is: {list}")