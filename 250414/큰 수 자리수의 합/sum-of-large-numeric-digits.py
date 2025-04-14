a, b, c = map(int, input().split())

t = a * b * c

def func(num, result):
    if num < 10:
        return(result + num)

    return func(num // 10, result + (num % 10))


print(func(t, 0))