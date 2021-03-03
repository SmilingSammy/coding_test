# [3차] 파일명 정렬
import re
def solution(files):
    sep_ls = []
    for f in files:
        f = f[:100]
        digit = re.findall("\d{1,5}", f)[0]
        f = re.sub(digit, "*", f)
        idx = f.index('*')
        head = f[:idx]
        tail = f[idx+1:].replace("*", digit)
        sep_ls.append([head, digit, tail])
    res_ls = sorted(sep_ls, key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(elem) for elem in res_ls]