# Lv3 외벽 점검
from itertools import permutations

def solution(n, weak, dist):
    l = len(weak)
    candidates = []

    w_point = weak + [w+n for w in weak]

    for i, start in enumerate(weak):
        for friends in permutations(dist):
            count = 1
            position = start

            for friend in friends:
                position += friend

                if position < w_point[i+l-1]:
                    count += 1
                    position = [w for w in w_point[i+1:i+l] if w > position][0]

                else:
                    candidates.append(count)
                    break

    return min(candidates) if candidates else -1