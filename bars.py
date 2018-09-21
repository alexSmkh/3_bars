import json
import sys
from json.decoder import JSONDecodeError


def load_data(file_name):
    with open(file_name, 'r', encoding="utf8") as file_holder:
        data_of_json_file = json.load(file_holder)
        return data_of_json_file


def get_biggest_bar(data_of_bars):
    the_biggest_bar = max(data_of_bars, key=lambda bar: bar['SeatsCount'])
    return the_biggest_bar


def get_smallest_bar(data_of_bars):
    the_smallest_bar = min(data_of_bars, key=lambda bar: bar['SeatsCount'])
    return the_smallest_bar


def get_closest_bar(data, longitude, latitude):
    pass


def print_the_biggest_bar(the_biggest_bar):
    print('The biggest bar is ' + the_biggest_bar['Name'])


def print_the_smallest_bar(the_smallest_bar):
    print('The smallest bar is ' + the_smallest_bar['Name'])


if __name__ == '__main__':
    try:
        json_file_name = sys.argv[1]
        data_from_json_file = load_data(json_file_name)
        print(type(data_from_json_file))
        print_the_biggest_bar(get_biggest_bar(data_from_json_file))
        print_the_smallest_bar(get_smallest_bar(data_from_json_file))

    except IndexError:
        print('You forgot to enter the file name.')
    except IOError:
        print('File not found')
    except JSONDecodeError:
        print('The file must be a json format')

