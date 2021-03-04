# [3차] 방금그곡
import re
from datetime import datetime
def solution(m, musicinfos):
    result = []
    for info in musicinfos:
        start, end, title, music = info.split(",")
        # minute
        minutes = (datetime.strptime(end, '%H:%M') - datetime.strptime(start, '%H:%M')).seconds // 60
        # 음표 추출
        music = re.findall("[A-Z]{1}\#{0,1}", music)
        music = (music * (minutes // len(music) + 1))[:minutes]
        #
        m_ls = re.findall("[A-Z]{1}\#{0,1}", m)
        idx_ls = [i for i in range(len(music)) if m_ls[0] == music[i]]
        for idx in idx_ls:
            if m == ''.join(music[idx:idx+len(m_ls)]):
                result.append([minutes, title])
                break
    if result:
        return sorted(result, key=lambda x: x[0], reverse=True)[0][1]
    else:
        return "(None)"