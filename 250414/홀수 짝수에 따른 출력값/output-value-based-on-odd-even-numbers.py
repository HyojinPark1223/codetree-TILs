N = int(input())

def func(num, score):
    score += num

    if num == N:
        return score

    return func(num + 2, score)

if N % 2 == 0:
    print(func(2, 0))
else:
    print(func(1, 0))