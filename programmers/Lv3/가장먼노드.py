def solution(n, vertex):
    node_dict = {k: [] for k in range(1, n+1)}
    for v in vertex:
        node_dict[v[0]].append(v[1])
        node_dict[v[1]].append(v[0])

    counts = [0 for i in range(n)]
    counts[0] = 1

    stack = []
    start = 1
    cases = list(map(lambda x: [start, x], node_dict[start]))
    stack += cases

    while stack:
        node = stack.pop(0)

        # 들렸으면 제외
        if counts[node[1]-1] != 0:
            continue

        counts[node[1]-1] += counts[node[0]-1] + 1
        start = node[1]
        cases = list(map(lambda x: [start, x], node_dict[start]))
        stack += cases

    return counts.count(max(counts))
