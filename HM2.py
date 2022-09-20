# 1 First
def f1(*args, **kwargs):
    s = 0

    for param in args:
        if type(param) == int or type(param) == float:
            s += param

    return s

print(f1(1, 5, -3, 'abc', [12, 56, 'cad']))
print(f1())
print(f1(2, 4, 'abc', param_1=2))


# 2 #total, even, odd
def f2(n):
    if n == 0:
        return 0, 0, 0

    total, even, odd = f2(n-1)
    total += n

    if n % 2 == 0:
        even += n
    else:
        odd += n

    return total, even, odd

n_total, n_even, n_odd = f2(5)
print('total =', n_total)
print('even = ', n_even)
print('odd = ', n_odd)



# Return the value inserted if the number is integer
def f3():
    x = input()

    try:
        x = int(x)
    except ValueError:
            x = 0

    return x

print(f3())