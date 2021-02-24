# 오픈채팅방
def solution(record):
    action_dict = {"Enter": "{uid}님이 들어왔습니다.",
                   "Leave": "{uid}님이 나갔습니다."}

    uid_dict = dict()
    answer = []
    for elem in record:
        elem_ls = elem.split(" ")

        if len(elem_ls) == 3:
            uid_dict[elem_ls[1]] = elem_ls[2]

        if elem_ls[0] in ("Enter", "Leave"):
            answer.append([action_dict[elem_ls[0]], elem_ls[1]])

    return list(map(lambda x : x[0].format(uid=uid_dict[x[1]]), answer))