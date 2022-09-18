def get_sum(n):
    if n == 0:
        return 0
    return n + get_sum(n-1)

# Example where n=10
print(get_sum(10))

number_list=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def calculate_odd_and_even():
    odd_number = 0
    even_number = 0
    for i in number_list:
        if i % 2 == 0:
            even_number = even_number + i
        else:
            odd_number = odd_number + i

    return (odd_number, even_number)

my_tuple = calculate_odd_and_even()
print(my_tuple)



