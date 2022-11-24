import itertools
from data.data_list import DataList
from utils.graphic import Graphic
from utils.constants import MAX_EXPENDITURE

import numpy as np


def force_brute(cost_invest, actions, final_list=None):
    if final_list is None:
        final_list = []
    if not actions:
        return sum(i[2] for i in final_list), final_list
    cost_invest1, cost_list1 = force_brute(cost_invest, actions[1:], final_list)
    cost = actions[0]
    if cost[1] <= cost_invest:
        cost_invest2, cost_list2 = force_brute(cost_invest - cost[1], actions[1:], final_list + [cost])
        if cost_invest1 < cost_invest2:
            return cost_invest2, cost_list2
    return cost_invest1, cost_list1


# def dynamique(capacite, elements):
#     matrice = [[0 for _ in range(capacite + 1)] for _ in range(len(elements) + 1)]
#
#     for i in range(1, len(elements) + 1):
#         for w in range(1, capacite + 1):
#             if elements[i-1][1] <= w:
#                 pass
#                 # matrice[i][w] = max(elements[i-1][2] + matrice[i-1][w-elements[i-1][1]], matrice[i-1][w])
#             else:
#                 matrice[i][w] = matrice[i-1][w]
#
#     # Retrouver les éléments en fonction de la somme
#     w = capacite
#     n = len(elements)
#     elements_selection = []
#
#     while w >= 0 and n >= 0:
#         e = elements[n-1]
#         if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
#             elements_selection.append(e)
#             w -= e[1]
#         n -= 1
#     return matrice[-1][-1], elements_selection


def optimized(self):
    data_list = DataList.get_data_from_csv(self)
    performance = DataList.add_performance(data_list)
    sort_list = DataList.sort_on_performance(performance)
    print(force_brute(MAX_EXPENDITURE, sort_list))
    # print(dynamique(MAX_EXPENDITURE, sort_list))



if __name__ == '__main__':
    optimized('action')
    # optimized('dataset1_Python+P7')
    # optimized('dataset2_Python+P7')
