class Command:
    def D(k, cnt):
        """ 현재 선택된 행에서 X칸 아래에 있는 행을 선택 """
        cnt = int(cnt)
        done = 0
        while done != cnt:
            k += 1
            if status[k] == 'O':
                done += 1
        return k

    def U(k, cnt):
        """ 현재 선택된 행에서 X칸 위에 있는 행을 선택 """
        cnt = int(cnt)
        done = 0
        while done != cnt:
            k -= 1
            if status[k] == 'O':
                done += 1
        return k

    def C(k, n):
        """ 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택 """
        status[k] = 'X'
        revise_ls.append(k)

        ascending = True if k < n - 1 else False
        while True:
            if ascending:
                k = k + 1
                if status[k] == 'O':
                    break

                if k == n - 1:
                    ascending = False

            else:
                k = k - 1
                if status[k] == 'O':
                    break
        return k

    def Z():
        """ 가장 최근에 삭제된 행을 원래대로 복구 """
        if revise_ls:
            revise_idx = revise_ls.pop()
            status[revise_idx] = 'O'


def solution(n, k, cmd):
    global revise_ls, status
    revise_ls = []
    status = ['O'] * n

    for cm in cmd:
        c = cm.split(' ')
        job = c[0]

        func = getattr(Command, job)
        if job == 'C':
            k = func(k, n)
        elif job == 'Z':
            func()
        else:
            k = func(k, c[1])

    return ''.join(status)