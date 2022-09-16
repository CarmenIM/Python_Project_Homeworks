
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

#print the initial list
print(my_list)

#sort in increasing order
my_list.sort()
print(my_list)

#sort in decreasing order
my_list = sorted(my_list, reverse=True)
print(my_list)

#get odd values
def get_odd_numbers(numbers):
    odd_numbers = []

    for number in numbers:
        if number % 2 == 1:
            odd_numbers.append(number)

    return odd_numbers
numbers = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(get_odd_numbers(numbers))

#get even values
def get_even_numbers(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers
numbers = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(get_even_numbers(numbers))
