import numpy as np

from data.data_list import DataList
from utils.constants import MAX_EXPENDITURE

def glouton(max_invest, action_list):
    """
    Create a lists that are the maximum investment sum.
    :param:
        int: maximum of invest
        list: action list
    :return:
        list:  best actions lists
    """
    sort_action = sorted(action_list, key=lambda x: x[3])
    final_list = []
    cost_invest = 0
    while sort_action:
        action = sort_action.pop()
        if action[1] + cost_invest <= max_invest and action[3] > 0.0:
            final_list.append(action)
            cost_invest += action[1]
    return sum(i[1] for i in final_list), sum(j[3] for j in final_list), final_list

def run(self):
    data_list = DataList.get_data_from_csv(self)
    performance = DataList.add_performance(data_list)
    sort_list = DataList.sort_on_performance(performance)
    final_list = glouton(MAX_EXPENDITURE, sort_list)
    print(f"\nTotal cost: {final_list[0]}€")
    print(f"Total return: {round(final_list[1], 2)}€ \n")
    print("Actions list:")
    print(np.array(final_list[2]))

if __name__ == '__main__':
    run('action')
    # run('dataset1_Python+P7')
    # run('dataset2_Python+P7')
