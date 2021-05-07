# Lv3 셔틀버스

def solution(n, t, m, timetable):
    crew = [int(t.split(":")[0]) * 60 + int(t.split(":")[1]) for t in timetable ]
    crew.sort()

    # 버스 시간, 승객 수, 마지막 탄 크루의 도착시간
    bus = [(540+t*i, 0, None) for i in range(n)]

    b_idx, c_idx = 0, 0

    while c_idx < len(crew):
        c = crew[c_idx]
        if b_idx == len(bus):
            break

        if c <= bus[b_idx][0] and bus[b_idx][1] < m:
            t, cnt, _ = bus[b_idx]
            bus[b_idx] = (t, cnt+1, c)
            c_idx += 1

        else:
            b_idx += 1

    answer = bus[-1][0]
    if bus[-1][2]:
        if bus[-1][1] == m:
            answer = bus[-1][2] - 1

    return '%02d:%02d' % (answer // 60, answer % 60)