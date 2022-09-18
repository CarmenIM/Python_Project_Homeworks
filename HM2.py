# 1 First
def my_function(*args, **kwargs):
    sum = 0

    for x in args:
        if type(x) == int or type(x) == float:
            sum =sum + x
    else:
        return sum


print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_function())
print(my_function(2, 4, 'abc', param_1=2))


# 2 Sum of even numbers selected from a value
maximum = int(input(" Please Enter the Maximum Value : "))
total = 0

for number in range(1, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))
        total = total + number

print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, total))

# Sum of odd numbers selected from a value

maximum = int(input(" Please Enter the Maximum Value : "))
Oddtotal = 0

for number in range(1, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, Oddtotal))


# Return the value inserted if the number is integer

user_input = input("Please enter the number here -> ")

try:
    int(user_input)
    it_is = user_input
except ValueError:
    it_is = 0

print(it_is)