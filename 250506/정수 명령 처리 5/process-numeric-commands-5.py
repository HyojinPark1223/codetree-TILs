N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back":
        num.append(int(line[1]))
    elif line[0] == "get":
        print(num[int(line[1]) - 1])
    elif line[0] == 'size':
        print(len(num))
    else:
        num.pop()
