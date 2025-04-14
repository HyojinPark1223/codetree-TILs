N = int(input())

def func(i, result):
    if i == 1:
        return result + i
    
    return func(i - 1, result + i)

print(func(N, 0))