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
    return the_biggest_bar


def get_smallest_bar(data_of_bars):
    the_smallest_bar = min(data_of_bars['features'],
                           key=lambda bar: bar['properties']['Attributes']
                           ['SeatsCount'])
    return the_smallest_bar


def get_closest_bar(data_of_bars, coordinate_longitude, coordinate_latitude):
    client_coordinate = (coordinate_longitude, coordinate_latitude)
    closest_bar = min(data_of_bars['features'],
                      key=lambda bar: vincenty(client_coordinate,
                                               bar['geometry']['coordinates']))
    return closest_bar


def print_bar(bar):
    print('Самый маленький бар - '
          + bar['properties']['Attributes']['Name'] + '. Там '
          + str(bar['properties']['Attributes']['SeatsCount'])
          + ' мест.')


def get_longitude():
    entered_longitude = float(input('Введите долготу: '))
    return entered_longitude


def get_latitude():
    entered_latitude = float(input('Введите широту: '))
    return entered_latitude


def print_nearest_bar(bar):
    print('Ближайший к Вам бар: ' + bar['properties']['Attributes']['Name'])


def get_file_name():
    file_name = sys.argv[1]
    return file_name


if __name__ == '__main__':
    try:
        json_file_name = get_file_name()
        data_from_json_file = load_data(json_file_name)
        biggest_bar = get_biggest_bar(data_from_json_file)
        smallest_bar = get_smallest_bar(data_from_json_file)
        print_bar(biggest_bar)
        print_bar(smallest_bar)
        longitude = get_longitude()
        latitude = get_latitude()
        nearest_bar = get_closest_bar(data_from_json_file, longitude, latitude)
        print_nearest_bar(nearest_bar)

    except IndexError:
        print('You forgot to enter the file name.')
    except IOError:
        print('File not found')
    except JSONDecodeError:
        print('The file must be a json format')
    except ValueError:
        print('Invalid input format')
