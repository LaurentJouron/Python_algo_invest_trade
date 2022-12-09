from data.data_list import DataList
from utils.constants import MAX_EXPENDITURE

import numpy as np

def brute_force(cost_invest, actions, final_list=None):
    """
    Create a lists that are maximum investment sum.
    :param:
        int: cost_invest (maximum cost the client wants to invest)
        list: action_list (name, cost, profit, performance)
        list: final_list free
    :return:
        list:  best actions lists
    """
    if final_list is None:
        final_list = []
    if not actions:
        return sum(i[1] for i in final_list), final_list
    cost_invest1, cost_list1 = brute_force(cost_invest, actions[1:], final_list)
    cost = actions[0]
    if cost[1] <= cost_invest:
        cost_invest2, cost_list2 = brute_force(cost_invest - cost[1], actions[1:], final_list + [cost])
        if cost_invest1 < cost_invest2:
            return cost_invest2, cost_list2
    return cost_invest1, cost_list1

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
    action_list = DataList.get_data_from_csv(self)
    performance = DataList.add_performance(action_list)
    sort_list_on_performance = DataList.sort_on_performance(performance)
    actions_lists = brute_force(MAX_EXPENDITURE, sort_list_on_performance)
    print(f"\nTotal cost: {actions_lists[0]}€")
    print(f"Total return: {DataList.get_profit(actions_lists[1])}€ \n")
    print("Actions list:")
    print(np.array(actions_lists[1]))

if __name__ == '__main__':
    run('action')
    # run('dataset1_Python+P7')
    # run('dataset2_Python+P7')
