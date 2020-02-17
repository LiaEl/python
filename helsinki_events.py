import argparse
import json
import requests
from bs4 import BeautifulSoup


def get_location():
    location = requests.get('https://ipapi.co/json')
    response = location.json()
    return response['latitude'], response['longitude']


def get_event(lat, lon):
    param_str = '{}, {}, {}'.format(lat, lon, 5)
    param = {
        'distance_filter': param_str,
        'limit':'1',
        'language_filter':'en'
    }
    response = requests.get('http://open-api.myhelsinki.fi/v1/events/',
                                    params=param)
    return response.json()


def get_event_coordinates(event_info):
    event_lat = event_info['data'][0]['location']['lat']
    event_lon = event_info['data'][0]['location']['lon']

    return event_lat, event_lon

def get_event_text(event_info):
    event_intro = event_info['data'][0]['description']['intro']
    event_body = event_info['data'][0]['description']['body']

    soup = BeautifulSoup(event_body, 'html.parser')
    event_text = soup.prettify()
    event_soup = BeautifulSoup(event_text, 'html.parser')

    return event_intro, event_soup.get_text()


def get_map_url(lat, lon):
    return f'http://maps.google.com/maps?q={lat}+{lon}'


def main():
    my_lat, my_lon = get_location()
    event_info = get_event(my_lat, my_lon)
    event_lat, event_lon = get_event_coordinates(event_info)
    event_intro, event_body = get_event_text(event_info)

    print(event_intro)
    print(event_body)
    print(get_map_url(event_lat, event_lon))




if __name__ == "__main__":
    main()