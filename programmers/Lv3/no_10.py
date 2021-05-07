# Lv3 합승 택시 요금
import heapq


def dijkstra(graph, start, end):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    queue = []
    heapq.heappush(queue, [dist[start], start])

    while queue:
        cur_dist, cur_dest = heapq.heappop(queue)

        if dist[cur_dest] < cur_dist:
            continue

        for new_dest, new_dist in graph[cur_dest].items():
            d = cur_dist + new_dist
            if d < dist[new_dest]:
                dist[new_dest] = d
                heapq.heappush(queue, [d, new_dest])

    return dist[end]


def solution(n, s, a, b, fares):
    graph = {}
    fare_all = fares + [[fare[1], fare[0], fare[2]] for fare in fares]

    for fare in fare_all:
        start, end, cost = fare
        if start not in graph:
            graph[start] = {}

        graph[start][end] = cost

    cost = float('inf')
    for i in list(graph.keys()):
        cost = min(cost, dijkstra(graph, s, i) + dijkstra(graph, i, a) + dijkstra(graph, i, b))

    return cost