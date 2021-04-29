# Lv3 불량 사용자
from itertools import product

def solution(user_id, banned_id):
    case_ls = []

    for ban in banned_id:
        ban_case = []

        for usr in user_id:

            if len(ban) != len(usr):
                continue

            done = True
            for b, u in zip(list(ban), list(usr)):
                if b == '*':
                    continue

                if b != u:
                    done = False
                    break

            if done:
                ban_case.append(usr)

        case_ls.append(ban_case)

    answer = set([tuple(sorted(x)) for x in product(*case_ls) if len(set(x)) == len(banned_id)])

    return len(answer)