_list_  = [1, 2, 3, 4, 5]
rm_occurance = list(set(_list_))
s_list = sorted(rm_occurance, reverse=True)
print("The second maximum element in the list is:", s_list[1])