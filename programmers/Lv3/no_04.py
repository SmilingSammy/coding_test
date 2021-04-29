# Lv3 추석 트래픽
def check_second_period(t, ls):
    count = 0
    start = t
    end = t + 1000

    for case in ls:
        if case[1] >= start and case[0] < end:
            count += 1

    return count


def solution(lines):
    ls = []
    max_count = 1

    for l in lines:
        _, hms, t = l.split()
        hms = list(map(float, hms.split(':')))
        t = float(t.replace('s', '')) * 1000

        end = (hms[0] * 3600 + hms[1] * 60 + hms[2]) * 1000
        start = end - t + 1

        ls.append([int(start), int(end)])

    for l in ls:
        max_count = max(max_count, check_second_period(l[0], ls), check_second_period(l[1], ls))

    return max_count