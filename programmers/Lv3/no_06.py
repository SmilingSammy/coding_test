# Lv3 매칭점수

import re


def solution(word, pages):
    p_dict = {}
    l_dict = {}

    for i, pg in enumerate(pages):

        pg = pg.lower()
        # url
        my_url = re.search(r'<meta[^>]*content="https://([\S]*)"/>', pg).group(1)

        if my_url not in p_dict:
            p_dict[my_url] = {}

        p_dict[my_url]['index'] = i

        # 기본점수
        b_score = 0
        for txt in re.findall(r'[a-z]+', pg):
            if txt == word.lower():
                b_score += 1

        p_dict[my_url]['b_score'] = b_score

        # 외부링크
        link_url = set()
        for url in re.findall(r'<a href="https://[\S]*">', pg):
            link_url.add(re.search(r'"https://([\S]*)"', url).group(1))

        link_url = list(link_url)

        p_dict[my_url]['link_no'] = len(link_url)

        for url in link_url:
            if url not in l_dict:
                l_dict[url] = []
            l_dict[url].append(my_url)

    result = []
    for key in p_dict.keys():
        m_score = p_dict[key]['b_score']

        if key in l_dict:
            for url in l_dict[key]:
                m_score += p_dict[url]['b_score'] / p_dict[url]['link_no']

        result.append([m_score, p_dict[key]['index']])

    return sorted(result, key=lambda x: [-x[0], x[1]])[0][1]
