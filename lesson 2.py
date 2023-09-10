# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# print(list_1.insert(2, 11))
# print(list_1)

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])
# print(list_1[1])
# print(list_1[len(list_1)-1]) # libo mojno pisat' prosche
# print(list_1[-1])
# print(list_1[-6])
# print(list_1[:]) # двоеточие значит, что мы выводим все элементы от начала до конца
# print(list_1[:2]) # выводим ДО второго элемента, не включая его
# print(list_1[len(list_1)-2:])
# print(list_1[2:9])
# print(list_1[::5])


# t = ()

# print (type(t))

# t = (1, 5, 3, )
# print (type(t))

# v = [1,8,9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# a,b,c = v

# print(a,b,c)

# t = (1,2,3,5,)

# print(t[1])

# for i in range(len(t)):
#     print(t[i])

# t = [1,2,3,5]

# t[0]=2

# print(t)

## СЛОВАРИ

# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d['q'])
# Пример

dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}

# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#    print('{}: {}'.format(item, dictionary[item]))

# print(dictionary.items())
# for (k,v) in dictionary.items():
#    print(k,v)

# # up: ↑
# # down: ↓
# # right: →


## Множества

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# q=set()

# Операции со множествами в Python

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}     это объединение
# i = a.intersection(b) # i = {8, 2, 5}            это пересечение
# dl = a.difference(b) # dl = {1, 3}               это разность а-б
# dr = b.difference(a) # dr = {13, 21}             это разность а-б
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# Замороженное множество
# a = {1, 8, 6}

# b = frozenset(a)

# print(a)