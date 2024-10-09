from collections import deque
from copy import deepcopy

K, M = map(int, input().split())
g = [list(map(int,input().split())) for _ in range(5)]

treasure = deque(list(map(int, input().split())))

class Board:
    def __init__(self):
        self.b = [[0] * 5 for _ in range(5)]

    def in_range(self, x, y):
        return 0 <= x < 5 and 0 <= y < 5

    def rotate(self, sx, sy, cnt):
        result = Board()
        result.b = deepcopy(self.b)

        if cnt == 0:
            for i in range(3):
                for j in range(3):
                    result.b[sx + i][sy + j] = self.b[sx + 2 - j][sy + i]
        elif cnt == 1:
            for i in range(3):
                for j in range(3):
                    result.b[sx + i][sy + j] = self.b[sx + 2 - i][sy + 2 - j]
        elif cnt == 2:
            for i in range(3):
                for j in range(3):
                    result.b[sx + i][sy + j] = self.b[sx + j][sy + 2 - i]

        return result

    def get_score(self):
        score = 0
        visit = [[False] * 5 for _ in range(5)]
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

        for i in range(5):
            for j in range(5):
                if not visit[i][j]:
                    q = deque([(i, j)])
                    trace = deque([(i, j)])

                    visit[i][j] = True
                    while q:
                        cur = q.popleft()
                        for k in range(4):
                            nx, ny = cur[0] + dx[k], cur[1] + dy[k]
                            if self.in_range(nx, ny) and self.b[nx][ny] == self.b[cur[0]][cur[1]] and not visit[nx][ny]:
                                q.append((nx, ny))
                                trace.append((nx, ny))
                                visit[nx][ny] = True

                    if len(trace) >= 3:
                        score += len(trace)
                        while trace:
                            t = trace.popleft()
                            self.b[t[0]][t[1]] = 0
        return score

    def fill(self, q):
        for i in range(5):
            for j in reversed(range(5)):
                if self.b[j][i] == 0:
                    self.b[j][i] = q.popleft()

board = Board()
board.b = deepcopy(g)

for _ in range(K):
    maxScore = 0
    maxScoreBoard = None

    for cnt in range(4):
        for sx in range(3):
            for sy in range(3):
                rotated = board.rotate(sx, sy, cnt)
                score = rotated.get_score()

                if maxScore < score:
                    maxScore = score
                    maxScoreBoard = rotated
    if maxScoreBoard is None:
        break
    board = maxScoreBoard

    while True:
        board.fill(treasure)
        newScore = board.get_score()
        if newScore == 0:
            break
        maxScore += newScore

    print(maxScore, end=" ")

#print('{} {}'.format(K, M))