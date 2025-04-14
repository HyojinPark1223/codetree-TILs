N = int(input())

def func(i, result):
    if i < 10:
        return result + (i ** 2)

    return func(i // 10, result + ((i % 10) ** 2))

print(func(N, 0))