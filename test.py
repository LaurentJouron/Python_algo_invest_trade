import itertools
from data.data_list import DataList
from utils.graphic import Graphic
from utils.constants import MAX_EXPENDITURE

import numpy as np


def naif(max_invest, action_list):
    sort_action = sorted(action_list, key=lambda x: x[3])
    final_list = []
    cost_invest = 0
    while sort_action:
        action = sort_action.pop()
        if action[1] + cost_invest <= max_invest:
            final_list.append(action)
            cost_invest += action[1]
    return sum(i[1] for i in final_list), final_list


def force_brute(cost_invest, actions, final_list=None):
    if final_list is None:
        final_list = []
    if not actions:
        return sum(i[1] for i in final_list), final_list
    cost_invest1, cost_list1 = force_brute(cost_invest, actions[1:], final_list)
    cost = actions[0]
    if cost[1] <= cost_invest:
        cost_invest2, cost_list2 = force_brute(cost_invest - cost[1], actions[1:], final_list + [cost])
        if cost_invest1 < cost_invest2:
            return cost_invest2, cost_list2
    return cost_invest1, cost_list1


def dynamique(max_invest, action_list):
    matrix = [[0 for _ in range(max_invest + 1)] for _ in range(len(action_list) + 1)]

    for i in range(len(action_list) + 1):
        for j in range(1, max_invest + 1):
            if action_list[i - 1][1] <= j:
                matrix[i][j] = max(action_list[i-1][1] + matrix[i-1][int(j-action_list[i-1][1])], matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]
    m = max_invest
    a = len(action_list)
    final_list: list = []

    while m >= 0 and a >= 0:
        e = action_list[a - 1]
        if matrix[a][m] == matrix[a-1][int(m - e[1])] + e[2]:
            final_list.append(e)
            m -= e[1]
        m -= 1
    return matrix[-1][-1], final_list


def optimized(self):
    data_list = DataList.get_data_from_csv(self)
    performance = DataList.add_performance(data_list)
    sort_list = DataList.sort_on_performance(performance)
    # print(naif(MAX_EXPENDITURE, sort_list))
    # print(force_brute(MAX_EXPENDITURE, sort_list))
    print(dynamique(MAX_EXPENDITURE, sort_list))


if __name__ == '__main__':
    optimized('action')
    # optimized('dataset1_Python+P7')
    # optimized('dataset2_Python+P7')
