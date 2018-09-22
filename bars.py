import json
import sys
from json.decoder import JSONDecodeError
from geopy.distance import vincenty


def load_data(file_name):
    with open(file_name, 'r', encoding='utf8') as file_holder:
        data_of_bars_from_json = json.load(file_holder)
        return data_of_bars_from_json['features']


def get_biggest_bar(data_of_bars):
    the_biggest_bar = max(data_of_bars,
                          key=lambda bar: bar['properties']['Attributes']
                                             ['SeatsCount'])
    print_bar(the_biggest_bar, 'big')


def get_smallest_bar(data_of_bars):
    the_smallest_bar = min(data_of_bars,
                           key=lambda bar: bar['properties']['Attributes'] \
                                              ['SeatsCount'])
    print_bar(the_smallest_bar, 'small')


def get_closest_bar(data_of_bars):
    longitude, latitude = get_coordinate()

    if longitude and latitude:
        client_coordinate = (longitude, latitude)
        closest_bar = min(data_of_bars,
                          key=lambda bar: vincenty(client_coordinate,
                                                   bar['geometry']
                                                      ['coordinates']))
        print_bar(closest_bar, 'closest')


def get_coordinate():
    try:
        longitude_coord = float(input('Введите долготу: '))
        latitude_coord = float(input('Введите широту: '))
        return longitude_coord, latitude_coord

    except (TypeError, ValueError):
        return None, None


def print_bar(bar, bar_type):
    bar_name = bar['properties']['Attributes']['Name']
    if bar_type == 'closest':
        print('Ближайший к Вам бар: ', bar_name)
    elif bar_type == 'small':
        print('Самый маленький бар: ', bar_name)
    elif bar_type == 'big':
        print('Самый большой бар: ', bar_name)


def get_file_name():
    try:
        file_name = sys.argv[1]
        return file_name

    except (IndexError, IOError, FileNotFoundError, JSONDecodeError):
        return None


if __name__ == '__main__':
    json_file_name = get_file_name()
    if json_file_name:
        data_from_json_file = load_data(json_file_name)
        get_biggest_bar(data_from_json_file)
        get_smallest_bar(data_from_json_file)
        get_closest_bar(data_from_json_file)
