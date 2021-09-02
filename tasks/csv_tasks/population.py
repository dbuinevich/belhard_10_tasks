"""
Написать функцию max_delta, в которой будет происходить чтение csv
файла world_population.csv и функцию должна возвращать год, в котором
наибольший процент прироста населения.
"""
import pandas


def max_delta(file):
    dict_from_csv = pandas.read_csv(file).to_dict()
    max_value = max(dict_from_csv['ChangePerc'].values())
    for key, value in dict_from_csv['ChangePerc'].items():
        if value == max_value:
            return dict_from_csv['Year'][key]


if __name__ == '__main__':
    print(max_delta('world_population.csv'))
