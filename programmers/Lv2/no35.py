# Lv2 순위검색

from itertools import combinations
import bisect


def search(scores, num):
    size = len(scores)
    return size - bisect.bisect_left(scores, num, lo=0, hi=size)


def solution(info, query):
    db = {}

    for i in info:
        tmp = i.split()
        conditions = tmp[:-1]
        score = int(tmp[-1])

        for n in range(5):
            combi = list(combinations(range(4), n))

            for c in combi:

                new_conditions = conditions.copy()

                for idx in c:
                    new_conditions[idx] = '-'

                condi = '/'.join(new_conditions)

                if condi in db:  # 모든 조건의 경우에 수에 대해 딕셔너리
                    db[condi].append(score)
                else:
                    db[condi] = [score]

    for value in db.values():
        value.sort()

    result = []

    for q in query:
        qry = q.replace(' and', '').split()

        q_cnd = '/'.join(qry[:-1])
        q_score = int(qry[-1])

        if q_cnd in db:
            data = db[q_cnd]
            result.append(search(data, q_score))

        else:
            result.append(0)

    return result