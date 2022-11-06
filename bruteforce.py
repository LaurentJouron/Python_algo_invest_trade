from utils.algo_invest import get_data_from_csv, add_performance, \
    sort_performance_list, get_cost_invest, get_best_profitability

MAX_EXPENDITURE: float = 500


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
    tempory_list: list = actions[i:]
    while get_cost_invest(tempory_list) > MAX_EXPENDITURE:
        tempory_list.pop()
    final_list.append(tempory_list)
    i += 1
    if i < len(tempory_list):
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
    final_cost: float = get_cost_invest(final_list)
    final_profit: float = round(get_best_profitability(final_list), 2)
    for i in range(len(action_list)):
        cost_action_list: float = get_cost_invest(action_list[i])
        profit_action_list: float = round(get_best_profitability(action_list[i]), 2)
        if final_profit < cost_action_list or final_cost < profit_action_list:
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
    action_list = get_data_from_csv(self)
    performance = add_performance(action_list)
    sort_list_on_performance = sort_performance_list(performance)
    actions_lists = create_actions_lists(sort_list_on_performance)
    compare = compare_actions_list(actions_lists)
    print(compare)


if __name__ == '__main__':
    brute_force('action')
    # brute_force('dataset1_Python+P7')
    # brute_force('dataset2_Python+P7')
