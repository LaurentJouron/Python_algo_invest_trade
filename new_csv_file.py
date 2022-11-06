import csv
import os

action_list = [
    ('Action-1', 20, 5),
    ('Action-2', 30, 10),
    ('Action-3', 50, 15),
    ('Action-4', 70, 20),
    ('Action-5', 60, 17),
    ('Action-6', 80, 25),
    ('Action-7', 22, 7),
    ('Action-8', 26, 11),
    ('Action-9', 48, 13),
    ('Action-10', 34, 27),
    ('Action-11', 42, 17),
    ('Action-12', 110, 9),
    ('Action-13', 38, 23),
    ('Action-14', 14, 1),
    ('Action-15', 18, 3),
    ('Action-16', 8, 8),
    ('Action-17', 4, 12),
    ('Action-18', 10, 14),
    ('Action-19', 24, 21),
    ('Action-20', 114, 18)
]


def create_csv_file(csv_name):
    if not exists_csv_file(f'data/{csv_name}.csv'):
        with open(f'data/{csv_name}.csv', 'w', newline='') as csvfile:
            fieldnames = ['Action', 'Cost', 'Profit']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for information in action_list:
                writer.writerow({'Action': information[0],
                                 'Cost': float(information[1]),
                                 'Profit': float(information[2])})


def exists_csv_file(path):
    return os.path.exists(f'data/{path}')


if __name__ == '__main__':
    create_csv_file('action')
