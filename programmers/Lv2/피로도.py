from itertools import permutations

def solution(k, dungeons):
    size = len(dungeons)
    cases = list(permutations(range(size), size))

    answer = []
    for case in cases:
        # 현재 피로도
        energy = k
        # 탐험 던전 수
        count = 0
        for c in case:
            # 최소 필요 필요도, 소모 피로도
            energy_limit, energy_usage = dungeons[c]
            if energy >= energy_limit:
                energy -= energy_usage
                count += 1
        answer.append(count)

    return max(answer)