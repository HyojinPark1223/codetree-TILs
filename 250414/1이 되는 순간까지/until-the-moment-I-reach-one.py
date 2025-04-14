N = int(input())

def func(num, cnt):
    if num == 1:
        return cnt
    
    if num % 2 == 0:
        return func(num // 2, cnt + 1)
    else:
        return func(num // 3, cnt + 1)
    

print(func(N, 0))