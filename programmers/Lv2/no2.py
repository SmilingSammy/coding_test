# 영어 끝말잇기
def solution(n, words):
    word_dict = dict()
    person, person_loc = 0, 0
    last_word = words[0][0]

    for idx, word in enumerate(words):
        if (word in word_dict) or (last_word != word[0]):
            person = n if (idx+1) % n == 0 else (idx+1) % n
            person_loc = (idx+1) // n + min((idx+1) % n, 1)
            return [person, person_loc]

        word_dict[word] = 1
        last_word = word[-1]

    return [person, person_loc]