n = int(input())
arr = list(map(int, input().split()))

def func(num, maxnum):
    if maxnum < arr[num]:
        maxnum = arr[num]

    if num == n - 1:
        return maxnum

    return(func(num + 1, maxnum))

print(func(0, 0))