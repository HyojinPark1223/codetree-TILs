import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

# value: key
table = {}

def call_init():
    global table
    table.clear()

def call_insert(name, value):
    global table

    if value not in [*table.keys()]:
        if name not in [*table.values()]:
            table[value] = name
            return 1
    return 0


def call_delete(name):
    global table

    if name not in table.items():
        return 0
    res_table = {v:k for k,v in table.items()}
    find_value = res_table.get(name)
    del table[find_value]
    return find_value

def call_rank(value):
    global table

    if len(table) < value:
        return None

    v_list = sorted(table.keys())

    return table[v_list[value-1]]

def call_sum(value):
    global table
    answer = 0
    v_list = sorted(table.keys())
    for v in v_list:
        if v > value:
            break
        answer += v

    return answer

for i in range(T):
    order = list(map(str, input().split()))

    # init
    if len(order) == 1:
        call_init()

    # insert
    elif len(order) == 3:
        print(call_insert(order[1], int(order[2])))

    else:
        o = order[0].upper()
        if o == 'DELETE':
            print(call_delete(order[1]))

        elif o == 'RANK':
            print(call_rank(int(order[1])))

        else:
            print(call_sum(int(order[1])))