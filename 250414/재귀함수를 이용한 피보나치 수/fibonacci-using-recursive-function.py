N = int(input())

def pibo(prev_num, cur_num, cnt):
    if cnt == N:
        return cur_num
    
    return pibo(cur_num, prev_num + cur_num, cnt + 1)

if N < 3:
    print(1)

print(pibo(1, 1, 2))