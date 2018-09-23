import json
import sys
from json.decoder import JSONDecodeError
from geopy.distance import vincenty


def load_data(file_name):
    try:
        with open(file_name, 'r', encoding='utf8') as file_holder:
            data_of_bars_from_json = json.load(file_holder)
            return data_of_bars_from_json['features']
    except (FileNotFoundError, JSONDecodeError):
        return None


def get_biggest_bar(bars):
    the_biggest_bar = max(
        bars,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount'],
    )
    return the_biggest_bar


def get_smallest_bar(bars):
    the_smallest_bar = min(
        bars,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount'],
    )
    return the_smallest_bar


def get_closest_bar(bars, longitude_coord, latitude_coord):
    if longitude_coord and latitude_coord:
        user_coordinates = (longitude_coord, latitude_coord)
        the_closest_bar = min(
            bars,
            key=lambda bar: vincenty(
                user_coordinates,
                bar['geometry']['coordinates'],
            )
        )
        return the_closest_bar


def get_user_coordinates():
    try:
        longitude_coord = float(input('Введите долготу: '))
        latitude_coord = float(input('Введите широту: '))
        return longitude_coord, latitude_coord

    except ValueError:
        return None, None


def print_bar(bar_name, bar_type):
    print(bar_type, bar_name)


def get_file_name():
    file_name = sys.argv[1]
    return file_name


if __name__ == '__main__':
    json_file_name = get_file_name()
    list_of_bars = load_data(json_file_name)

    if list_of_bars:
        biggest_bar = get_biggest_bar(list_of_bars)
        smallest_bar = get_smallest_bar(list_of_bars)

        print_bar(
            biggest_bar['properties']['Attributes']['Name'],
            'Самый маленький бар: ',
        )

        print_bar(
            smallest_bar['properties']['Attributes']['Name'],
            'Самый маленький бар: ',
        )

    longitude, latitude = get_user_coordinates()
    if longitude and latitude:
        closest_bar = get_closest_bar(list_of_bars, latitude, longitude)

        print_bar(
            closest_bar['properties']['Attributes']['Name'],
            'Ближайший к Вам бар: ',
        )


