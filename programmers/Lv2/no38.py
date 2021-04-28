# Lv2 수식최대화

import re
from itertools import permutations
from copy import copy


def calculate(num1, num2, op):
    if op == '-':
        return num1 - num2
    elif op == '+':
        return num1 + num2
    else:
        return num1 * num2


def solution(expression):
    nums = list(map(int, re.split('\D', expression)))
    operands = re.findall('\D', expression)

    operand_unique = list(set(operands))
    operand_combi = list(permutations(operand_unique, len(operand_unique)))

    candidate = []

    for combi in operand_combi:
        tmp_nums = copy(nums)
        tmp_ops = copy(operands)

        for op in combi:
            op_count = tmp_ops.count(op)

            for _ in range(op_count):
                op_idx = tmp_ops.index(op)

                num1, num2 = tmp_nums[op_idx], tmp_nums[op_idx + 1]
                new_num = calculate(num1, num2, op)

                del tmp_nums[op_idx]
                del tmp_nums[op_idx]
                del tmp_ops[op_idx]

                tmp_nums.insert(op_idx, new_num)

        candidate.append(abs(tmp_nums[0]))

    return max(candidate)