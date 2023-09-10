# task1

list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
i = 0
lst = []
for i in range(len(list_1)):
    if list_1[i] not in lst:
        lst.append(list_1[i])
print (lst, end= ',')
print (len(set(lst)))

#task2
