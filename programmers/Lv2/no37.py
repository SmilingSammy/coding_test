## Lv2 문자열 압축

def solution(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1

    for cut in range(1, len(s) // 2 + 1):
        count = 1
        candidate = s[:cut]

        for i in range(cut, len(s), cut):
            if s[i:i + cut] == candidate:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + candidate
                candidate = s[i:i + cut]
                count = 1

        if count == 1:
            count = ""

        result += str(count) + candidate
        length.append(len(result))
        result = ""

    return min(length)