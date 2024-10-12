dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

class Player():
    def __init__(self):
        self.id = 0
        self.coor = (0, 0)
        self.d = 0
        self.hp = 0
        self.gun = 0
        self.point = 0

n, m, k = map(int, input().split())
gun_map = [list(map(int, input().split())) for _ in range(n)]
p_map = [[-1] * n for _ in range(n)]
gun_info = {}
players = []

for i in range(n):
    for j in range(n):
        if gun_map[i][j] > 0:
            gun_info[(i, j)] = [gun_map[i][j]]
            gun_map[i][j] = True
        else:
            gun_map[i][j] = False

for i in range(m):
    x, y, d, s = map(int, input().split())
    p = Player()
    p.id = i
    p.coor = (x-1, y-1)
    p.d = d
    p.hp = s
    p_map[x-1][y-1] = i

    players.append(p)

# ==================================

def in_range(x, y):
    global n
    return 0 <= x < n and 0 <= y <n

def move(id, isFight):
    global players, p_map

    meetWall = 0
    (x, y) = players[id].coor

    for d in range(4):
        di = (players[id].d + d + 4 + meetWall) % 4
        nx, ny = x + dx[di], y + dy[di]

        if in_range(nx, ny):
            # 아무 것도 없음(이동 가능)
            if p_map[nx][ny] < 0:
                p_gun = players[id].gun
                if gun_map[nx][ny]:
                    for g in range(len(gun_info[(nx, ny)])):
                        if gun_info[(nx, ny)][g] > p_gun:
                            p_gun, gun_info[(nx, ny)][g] = gun_info[(nx, ny)][g], p_gun

                    if max(gun_info[(nx, ny)]) == 0:
                        del gun_info[(nx, ny)]
                        gun_map[nx][ny] = False

                players[id].coor = (nx, ny)
                players[id].gun = p_gun
                players[id].d = di

                p_map[nx][ny] = id
                if not isFight:
                    p_map[x][y] = -1
                return

            # 사람이 있음
            else:
                # 싸운적 없음: 대결
                if not isFight:
                    winner, loser, point = fight(id, p_map[nx][ny])

                    # 진 사람은 총 버리고 방향을 바꿔 이동
                    l_gun, players[loser].gun = players[loser].gun, 0

                    # 원래 자리에 총이 있으면 총 추가
                    if gun_map[nx][ny]:
                        gun_info[(nx, ny)].append(l_gun)
                    # 없으면 새로 총 추가
                    else:
                        gun_map[nx][ny] = True
                        gun_info[(nx, ny)] = [l_gun]

                    # 이긴 사람은 자리에 남음
                    w_gun = players[winner].gun
                    if gun_map[nx][ny]:
                        for g in range(len(gun_info[(nx, ny)])):
                            if gun_info[(nx, ny)][g] > w_gun:
                                w_gun, gun_info[(nx, ny)][g] = gun_info[(nx, ny)][g], w_gun

                        if max(gun_info[(nx, ny)]) == 0:
                            del gun_info[(nx, ny)]
                            gun_map[nx][ny] = False

                    players[winner].coor = (nx, ny)
                    players[winner].gun = w_gun
                    players[winner].point += point

                    p_map[nx][ny] = winner
                    p_map[x][y] = -1

                    players[loser].coor = (nx, ny)
                    move(loser, True)
                    return
                # 싸움: 다른 방향으로 탐색 진행ㅠ
        else:
            if not isFight:
                meetWall += 1

def fight(m_id, p_id):
    global players
    winner, loser, point = 0, 0, 0
    m_power = players[m_id].hp + players[m_id].gun
    p_power = players[p_id].hp + players[p_id].gun

    if m_power > p_power:
        winner = m_id
        loser = p_id
        point = m_power - p_power

    elif m_power == p_power:
        if players[m_id].hp > players[p_id].hp:
            winner = m_id
            loser = p_id
        else:
            winner = p_id
            loser = m_id
    else:
        winner = p_id
        loser = m_id
        point = p_power - m_power

    return winner, loser, point

# ==================================
#pprint.pprint(gun_map)
#pprint.pprint(p_map)

for _ in range(k):
    for i in range(m):
        move(i, False)
        #pprint.pprint(gun_map)
        #pprint.pprint(p_map)
        #print(players[i].id, "=", players[i].coor, players[i].gun)
        #pprint.pprint(gun_info)
    #print("####################")
#answer = []
for i in range(m):
    #answer.append(players[i].point)
    print(players[i].point, end=' ')