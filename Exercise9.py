list1 = [20,23,27,31,33,35,37]
list2 = [2,4,6,8,10,12,14,1]
new_list = []
for num in list1:
    if num % 2 == 1:
        new_list.append(num)
for num in list2:
    if num % 2 == 0:
        new_list.append(num)
print("Our new list = ", new_list)
