# Lv3 단어 변환
def transform(word, trf_word, count):
    zero_count = [1 if x==y else 0 for x, y in zip(list(word), list(trf_word))].count(0)

    if zero_count != 1:
        return (word, count)
    else:
        return (trf_word, count+1)

def solution(begin, target, words):
    if target not in words:
        return 0

    case = [(begin, 0)]
    while case:
        s, c = case.pop(0)
        for w in words:
            new_s, new_c = transform(s, w, c)
#             print(s,c, w, new_s, new_c, case)
            if new_s == target:
                return new_c

            else:
                if s != new_s:
                    case.append((new_s, new_c))
