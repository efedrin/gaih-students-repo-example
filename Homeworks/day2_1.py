list = [1,2,3,"a","b","c"]
n = len(list)
list1 = list[:n//2]
list2 = list[n//2:]
list = list2 + list1
print(list)
