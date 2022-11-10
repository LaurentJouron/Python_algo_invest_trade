import matplotlib.pyplot as plt


class Graphic:
    @staticmethod
    def get_ordered_y(actions):
        """
        Function that retrieves the ordinates (y), according to a list.
        :param:
            list: action_list (name, cost, profit, performance)
        :return:
            list:  float of orderer
        """
        return [[float(actions[i][1])] for i in range(len(actions))]

    @staticmethod
    def get_abcissa_x(actions):
        """
        Function that retrieves abcissa(x), according to a list.
        :param:
            list: action_list (name, cost, profit, performance)
        :return:
            list:  float of abcissa
        """
        return [[float(actions[i][2])] for i in range(len(actions))]

    @staticmethod
    def get_graphic(x, y):
        """
        function plots a graph according to abcissa and ordinates.
        :param:
            list: abcissa (10.20, 53.2, etc...)
            list: orderer (25.3, 45.7, etc...)
        :return:
            graphic
        """
        plt.scatter(x, y)
        plt.xlabel('2 year profit')
        plt.ylabel('Investment cost')
        return plt.show()
