from utils.data_list import DataList as DL
from utils.constants import MAX_EXPENDITURE

# import numpy as np
# import matplotlib.pyplot as plt


def create_actions_lists(actions, final_list=None, i: int = 0):
    """
    Create a lists that are optimized on the maximum investment sum.
    :param:
        list: action_list (name, cost, profit, performance)
        list: final_list free
        int: 0 at initialization and +1 at each recursion
    :return:
        list:  best actions lists
    """
    if final_list is None:
        final_list = []
    temporary_list: list = actions[i:]
    while DL.get_cost_invest(temporary_list) > MAX_EXPENDITURE:
        temporary_list.pop()
    final_list.append(temporary_list)
    i += 1
    if i < len(temporary_list):
        create_actions_lists(actions, final_list, i)
    return final_list


def compare_actions_list(action_list):
    """
    compare an action list in the best investment and profitability.
    :param:
        list: action_list (name, cost, profit, performance)
    :return:
        list:  best action list
    """
    final_list: list = []
    if not final_list:
        final_list.extend(action_list[0])
    final_cost: float = DL.get_cost_invest(final_list)
    final_profit: float = round(DL.get_profit(final_list), 2)
    for i in range(len(action_list)):
        cost: float = DL.get_cost_invest(action_list[i])
        profit: float = round(DL.get_profit(action_list[i]), 2)
        if cost > final_cost and profit > final_profit:
            final_list.clear()
            final_list.extend(action_list[i])
    return final_list


def brute_force(self):
    """
    Build the query according to, calling all the preamble functions create.
    :param:
        str: file_name (csv)
    :return:
        list: best solution
    """
    action_list = DL.get_data_from_csv(self)
    performance = DL.add_performance(action_list)
    sort_list_on_performance = DL.sort_on_performance(performance)
    actions_lists = create_actions_lists(sort_list_on_performance)
    compare = compare_actions_list(actions_lists)
    print(f"\nTotal cost: {round(DL.get_cost_invest(compare), 2)}€")
    print(f"Total return: {round(DL.get_profit(compare), 2)}€ \n")
    print("Actions list:")
    for i in range(len(compare)):
        print(f" - {compare[i][0]}")


if __name__ == '__main__':
    brute_force('action')
    # brute_force('dataset1_Python+P7')
    # brute_force('dataset2_Python+P7')
