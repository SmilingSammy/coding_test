# [3차] 압축

import string
def solution(s):
    idx_ls = []
    last_num = 27
    lzw_dict = {key: (num+1) for num, key in enumerate(list(string.ascii_uppercase))}

    while s != '':
        pos_case = list(filter(lambda x: x == s[:len(x)], lzw_dict.keys()))
        w = sorted(pos_case, key=lambda x: len(x), reverse=True)[0]

        # idx num append
        idx_ls.append(lzw_dict[w])
        # dict update
        lzw_dict[s[:len(w)+1]] = last_num
        last_num += 1
        s = s[len(w):]

    return idx_ls
