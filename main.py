#Homework number 1

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# print the initial list
print(my_list)

# sort from least to greatest
my_list.sort()
print(my_list)

# sort from greatest to least
my_list = sorted(my_list, reverse=True)
print(my_list)

# list with even numbers
res = my_list[::2]
# print result
print(str(res))

# list with odd numbers
res = my_list[1::2]
# print result
print(str(res))

# divided by 3
for i in my_list:
    if i % 3 != 0:
        continue
    print(f'can be divided by 3 -> {i}')



