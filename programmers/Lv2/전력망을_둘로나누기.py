from collections import defaultdict


def dfs(x, visit):
    global count
    visit.append(x)
    count += 1

    for i in tree[x]:
        if i not in visit:
            dfs(i, visit)


def solution(n, wires):
    global tree, count
    tree = defaultdict(list)
    result = []

    for x, y in wires:
        tree[x].append(y)
        tree[y].append(x)

    for x, y in wires:
        # wire cut
        tree[x].remove(y)
        tree[y].remove(x)

        count = 0
        dfs(1, [])
        # 개수: count, n-count --> 둘 차이 n-count-count
        result.append(abs(n - count * 2))

        # wire restore
        tree[x].append(y)
        tree[y].append(x)

    return min(result)