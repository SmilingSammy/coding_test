# 방문 길이
def solution(dirs):
    cmd_dict = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    x, y = 0, 0
    result = set()

    for cmd in dirs:
        _x, _y = cmd_dict[cmd]
        new_x, new_y = x + _x, y + _y

        if new_x > 5 or new_x < -5 or new_y > 5 or new_y < -5:
            continue

        path1 = (x, y, new_x, new_y)
        path2 = (new_x, new_y, x, y)

        if path1 not in result:
            result.add(path1)
            result.add(path2)

        x, y = new_x, new_y

    return len(list(result)) // 2