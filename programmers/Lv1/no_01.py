# 폰켓몬 (Lv1)
def solution(nums):
    get_num = len(nums) // 2
    return len(list(set(nums))[:get_num])