import pprint

from collections import deque

def print_arr(arrs):
    for i in range(len(arrs)):
        for j in range(len(arrs)):
            print(arrs[i][j], end=" ")
        print()


def arr_copy(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] = arr2[i][j]


def rotate(sx, sy, rr):
    tmp = [[0] * 3 for _ in range(3)]
    result = [[0] * 3 for _ in range(3)]

    len_tmp = 3

    for i in range(3):
        for j in range(3):
            tmp[i][j] = arr[sx + i][sy + j]

    for i in range(len_tmp):
        for j in range(len_tmp):
            if rr == 0:
                result[j][len_tmp - i - 1] = tmp[i][j]  # 시계
            elif rr == 1:
                result[len_tmp - i - 1][len_tmp - j - 1] = tmp[i][j]  # 시계 180
            else:
                result[len_tmp - j - 1][i] = tmp[i][j]  # 시계 270

    for i in range(len_tmp):
        for j in range(len_tmp):
            arr[i + sx][j + sy] = result[i][j]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, c):
    global nn
    v = [[False] * nn for _ in range(nn)]
    q = deque()
    q.append([x, y, c])
    v[x][y] = True

    selected = []
    selected.append([x, y])

    while len(q) != 0:
        px, py, pc = q.popleft()

        for d in range(4):
            nx = px + dx[d]
            ny = py + dy[d]

            if nx < 0 or nx >= nn or ny < 0 or ny >= nn or v[nx][ny] == True or arr[nx][ny] != pc:
                continue

            q.append([nx, ny, pc])
            selected.append([nx, ny])
            v[nx][ny] = True

    if len(selected) >= 3:
        for ii, jj in selected:
            arr[ii][jj] = 0
        return len(selected)

    return 0


def get_value():
    global nn
    gval = 0
    for i in range(nn):
        for j in range(nn):
            if arr[i][j] != 0:
                gval += bfs(i, j, arr[i][j])

    return gval


def fill():
    global ww, nn

    for j in range(nn):
        for i in range(nn - 1, -1, -1):
            if arr[i][j] == 0:
                arr[i][j] = wall[ww]
                ww += 1


def get_real_value():
    global ans

    while True:
        now_ans = 0
        for i in range(nn):
            for j in range(nn):
                if arr[i][j] != 0:
                    now_ans += bfs(i, j, arr[i][j])
        if now_ans == 0:
            break
        else:
            # 정답 갱신
            ans += now_ans

            # 유물 채우기
            fill()


def pick():
    global nn
    pval = 0
    px = -1
    py = -1
    pr = -1
    for i in range(3):
        for j in range(3):
            for r in range(3):
                arr_copy(arr, ori_arr)

                # 이번에 찾을 위치 회전 시키기
                rotate(i, j, r)

                # 회전 시킨 유물의 1차 획득 가치 확인
                gval = get_value()

                if gval == 0:
                    continue

                if pval < gval:
                    pval = gval
                    px = i
                    py = j
                    pr = r
                elif pval == gval:
                    if pr > r:
                        px = i
                        py = j
                        pr = r
                    elif pr == r:
                        if py > j:
                            px = i
                            py = j
                            pr = r
                        elif py == j:
                            if px > i:
                                px = i
                                py = j
                                pr = r

    return px, py, pr


kk, mm = list(map(int, input().split()))

nn = 5

ori_arr = []
arr = [[0] * nn for _ in range(nn)]
v = [[False] * nn for _ in range(nn)]

for i in range(nn):
    ori_arr.append(list(map(int, input().split())))

wall = list(map(int, input().split()))
ww = 0

# 횟수만큼 반복
ss = 0
while ss < kk:
    # 회전 목표 선택
    xx, yy, rr = pick()

    # 회전해서 없을 수 있는 값이 없으면 끝내기
    if xx == -1:
        break

    # 회전
    arr_copy(arr, ori_arr)
    rotate(xx, yy, rr)

    # 끝까지 유물 획득
    ans = 0
    get_real_value()

    # 이번 턴에 획득한 유물이 없으면 끝내기
    if ans == 0:
        break

    # 출력
    print(ans, end=" ")

    # 원본 배열 수정
    arr_copy(ori_arr, arr)
    ss += 1