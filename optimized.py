import numpy as np

from data.data_list import DataList
from utils.constants import MAX_EXPENDITURE

def optimized(actions, final_list=None, i: int = 0):
    """
    returns an action list with the best investment and profitability.
    :param:
        list: action_list (name, cost, profit, performance)
        list: final_list Empty list at initialization
        int: an integer set to 0
    :return:
        list: action list with best on first
    """
    j: int = i
    if final_list is None:
        final_list = []
    temporary_list: list = []
    cost_invest: float = 0.0
    while cost_invest < MAX_EXPENDITURE and j < len(actions):
        cost_invest += actions[j][1]
        if cost_invest <= MAX_EXPENDITURE and actions[j][3] > 0.0:
            temporary_list.append(actions[j])
        else:
            cost_invest -= actions[j][1]
        j += 1
    final_list.append(temporary_list)
    i += 1
    if i < len(actions):
        optimized(actions, final_list, i)
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
    for i in range(len(action_list)):
        final_cost: float = DataList.get_cost_invest(final_list)
        final_profit: float = round(DataList.get_profit(final_list), 2)
        cost: float = DataList.get_cost_invest(action_list[i])
        profit: float = round(DataList.get_profit(action_list[i]), 2)
        if cost > final_cost and profit > final_profit:
            final_list.clear()
            final_list.extend(action_list[i])
    return final_list

def run(self):
    """
    Build the query according to, calling all the preamble functions create.
    :param:
        str: file_name (csv)
    :return:
        float: investment cost
        float: profit value
        list: best solution
    """
    data_list = DataList.get_data_from_csv(self)
    performance = DataList.add_performance(data_list)
    sort_list_on_performance = DataList.sort_on_performance(performance)
    actions_lists = optimized(sort_list_on_performance)
    compare = compare_actions_list(actions_lists)
    print(f"\nTotal cost: {round(DataList.get_cost_invest(compare), 2)}€")
    print(f"Total return: {round(DataList.get_profit(compare), 2)}€ \n")
    print("Actions list:")
    print(np.array(compare))

if __name__ == '__main__':
    run('action')
    # run('dataset1_Python+P7')
    # run('dataset2_Python+P7')
