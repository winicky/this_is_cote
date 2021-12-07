from itertools import combinations

# Method 1: dfs()
# Method 2: find_result(): using combinations

# input
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]

index = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            index.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


# def dfs(count):
#     global result
#
#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = graph[i][j]
#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(i, j)
#
#         result = max(result, get_score())
#         return
#
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 graph[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 graph[i][j] = 0
#                 count -= 1

def find_result():
    global result
    for v1, v2, v3 in list(combinations(index, 3)):
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        temp[v1[0]][v1[1]] = 1
        temp[v2[0]][v2[1]] = 1
        temp[v3[0]][v3[1]] = 1

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())


# dfs(0)
find_result()

print(result)


# input 01
# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

# input 02
# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2

# input 03
# 8 8
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
