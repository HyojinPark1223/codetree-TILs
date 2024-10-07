from collections import deque

Q = int(input())
nodes = {}
nodeInfo = {}
topNode = []

def checkDepth(parents):
    global nodes, nodeInfo
    nodecnt = 2
    checkList = deque([parents])

    while checkList:
        p = checkList.popleft()
        detph = nodeInfo[p][2]

        if nodecnt > detph:
            return False

        if nodeInfo[p][0] != -1:
            checkList.append(nodeInfo[p][0])
    return True

# 노드 추가
def addNode(id, parents, color, depth):
    global nodes, nodeInfo, topNode
    # 최상위 노드
    if parents < 0:
        nodes[id] = []
        topNode.append(id)

    # 그 외
    else:
        if not checkDepth(parents):
            return
        nodes[parents].append(id)
        if id not in nodes:
            nodes[id] = []

    # 겹칠 일 없다고 하였으니 바로 dict에 넣어줌.
    nodeInfo[id] = [parents, color, depth]

# 노드 색 변경
def changeColor(id, color):
    global nodes, nodeInfo

    nodeInfo[id][1] = color
    changed = [id]
    q = deque(nodes[id])

    while q:
        baby_node = q.popleft()
        if baby_node not in changed:
            nodeInfo[baby_node][1] = color
            q.extend(nodes[baby_node])
            changed.append(baby_node)

# 컬러 합 구하기
def countAllColor(id):
    global nodes, nodeInfo
    q = deque([id])
    colorlist = []
    while q:
        node = q.popleft()
        colorlist.append(nodeInfo[node][1])
        q.extend(nodes[node])

    return set(colorlist)

# 점수 조회
def calScore():
    global nodes, nodeInfo, topNode

    q = deque(topNode)
    cntList = []
    # 가치의 제곱의 합
    while q:
        node = q.popleft()
        cntList.append(countAllColor(node))
        q.extend(nodes[node])

    return cntList

# def main
for i in range(Q):
    orders = list(map(int, input().split()))

    # 100(노드 추가)
    if len(orders) == 5:
        addNode(orders[1], orders[2], orders[3], orders[4])

    # 200(색 변경)
    elif len(orders) == 3:
        changeColor(orders[1], orders[2])

    # 300(색 조회)
    elif len(orders) == 2:
        print(nodeInfo[orders[1]][1])

    # 400(점수 조회)
    else:
        answerList = calScore()
        sum_color = 0
        for colorlist in answerList:
            sum_color += (len(colorlist) ** 2)
        print(sum_color)