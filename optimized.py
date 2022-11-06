from utils.algo_invest import get_data_from_csv, add_performance, \
    sort_performance_list, get_cost_invest, get_best_profitability


MAX_EXPENDITURE: float = 500


def get_best_action_list(actions, final_list=None, i: int = 0):
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
    tempory_list: list = []
    cost_invest: float = 0.0
    while cost_invest < MAX_EXPENDITURE and j < len(actions):
        cost_invest += actions[j][1]
        if cost_invest <= MAX_EXPENDITURE:
            tempory_list.append(actions[j])
        else:
            cost_invest -= actions[j][1]
        j += 1
    final_list.append(tempory_list)
    i += 1
    if i < len(actions):
        get_best_action_list(actions, final_list, i)
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
        final_cost: float = get_cost_invest(final_list)
        final_profit: float = round(get_best_profitability(final_list), 2)
        cost_action_list: float = get_cost_invest(action_list[i])
        profit_action_list: float = round(get_best_profitability(action_list[i]), 2)
        if final_cost < cost_action_list and final_profit < profit_action_list:
            final_list.clear()
            final_list.extend(action_list[i])
    return final_list


def optimized(self):
    data_list = get_data_from_csv(self)
    performance = add_performance(data_list)
    sort_list_on_performance = sort_performance_list(performance)
    best_actions_list = get_best_action_list(sort_list_on_performance)
    compare = compare_actions_list(best_actions_list)
    print(compare)


if __name__ == '__main__':
    optimized('action')
    # optimized('dataset1_Python+P7')
    # optimized('dataset2_Python+P7')