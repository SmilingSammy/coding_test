# Lv3 보석쇼핑

def solution(gems):
    jewerly_size = len(set(gems))
    gem_size = len(gems)
    answer = [0, gem_size - 1]
    start, end = 0, 0

    j_dict = {gems[0]: 1}

    while start < gem_size and end < gem_size:
        if len(j_dict) == jewerly_size:
            if answer[1] - answer[0] > end - start:
                answer[0] = start
                answer[1] = end
            if j_dict[gems[start]] == 1:
                del j_dict[gems[start]]
            else:
                j_dict[gems[start]] -= 1

            start += 1

        else:
            end += 1
            if end == gem_size:
                break
            else:
                if j_dict.get(gems[end]) is None:
                    j_dict[gems[end]] = 1
                else:
                    j_dict[gems[end]] += 1

    answer = list(map(lambda x: x+1, answer))
    return answer