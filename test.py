from data.data_list import DataList
from utils.graphic import Graphic
# from utils.constants import MAX_EXPENDITURE

import numpy as np


def get_array(actions):
    return np.array(actions)


def get_only_positif(action):
    return [action[i] for i in range(len(action)) if float(action[i][1]) > 0.0]


def test(self):
    data_list = DataList.get_data_from_csv(self)
    performance = DataList.add_performance(data_list)
    positif = get_only_positif(performance)
    sort_performance = DataList.sort_on_performance(positif)
    action_array = get_array(sort_performance)
    ordered_y = Graphic.get_ordered_y(action_array)
    abcissa_x = Graphic.get_abcissa_x(action_array)
    Graphic.get_graphic(abcissa_x, ordered_y)


if __name__ == '__main__':
    test('action')
    # test('dataset1_Python+P7')
    # test('dataset2_Python+P7')
