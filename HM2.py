# 1
def my_function(*param_1,**param_2):
    sum = 0
    if type(param_2) == float:
        sum += param_1
    for x in param_1:
        if type(x) == int or type(x) == float:
            sum += x
    else:
        return sum


print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_function())
print(my_function(2, 4, 'abc', param_1=2))

# 2
def get_sum(n):
    if n == 0:
        return 0
    return n + get_sum(n-1)

# Example where n=10
print(get_sum(10))






