import json
import sys
from json.decoder import JSONDecodeError
from geopy.distance import vincenty


def load_data(file_name):
    with open(file_name, 'r', encoding="utf8") as file_holder:
        data_of_json_file = json.load(file_holder)
        return data_of_json_file


def get_biggest_bar(data_of_bars):
    the_biggest_bar = max(data_of_bars['features'],
                          key=lambda bar: bar['properties']['Attributes']
                          ['SeatsCount'])
    print_biggest_bar(the_biggest_bar)


def get_smallest_bar(data_of_bars):
    the_smallest_bar = min(data_of_bars['features'],
                           key=lambda bar: bar['properties']['Attributes']
                           ['SeatsCount'])
    print_smallest_bar(the_smallest_bar)


def get_closest_bar(data_of_bars):
    longitude = get_longitude()
    latitude = get_latitude()

    client_coordinate = (longitude, latitude)
    closest_bar = min(data_of_bars['features'],
                      key=lambda bar: vincenty(client_coordinate,
                                               bar['geometry']['coordinates']))
    print_nearest_bar(closest_bar)


def get_longitude():
    entered_longitude = float(input('Введите долготу: '))
    return entered_longitude


def get_latitude():
    entered_latitude = float(input('Введите широту: '))
    return entered_latitude


def print_nearest_bar(bar):
    print('Ближайший к Вам бар: ' + bar['properties']['Attributes']['Name'])


def print_smallest_bar(small_bar):
    print('Самый маленький бар - '
          + small_bar['properties']['Attributes']['Name'] + '. Там '
          + str(small_bar['properties']['Attributes']['SeatsCount'])
          + ' мест.')


def print_biggest_bar(big_bar):
    print('Самый большой бар - '
          + big_bar['properties']['Attributes']['Name'] + '. Там '
          + str(big_bar['properties']['Attributes']['SeatsCount'])
          + ' мест.')


def get_file_name():
    file_name = sys.argv[1]
    return file_name


if __name__ == '__main__':
    try:
        json_file_name = get_file_name()
        data_from_json_file = load_data(json_file_name)
        get_biggest_bar(data_from_json_file)
        get_smallest_bar(data_from_json_file)
        get_closest_bar(data_from_json_file)

    except IndexError:
        print('You forgot to enter the file name.')
    except IOError:
        print('File not found')
    except JSONDecodeError:
        print('The file must be a json format')
    except ValueError:
        print('Invalid input format')
