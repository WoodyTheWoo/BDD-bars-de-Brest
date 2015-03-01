# -*- coding: utf-8 -*-

"""
    Created by : Joe
"""

import json
import urllib.request
import sqlite_handler
import key


def main():
    print('Bars_Brest - bars.py')

    sqlite_handler.check_db()

    i = 0

    for res in parse_global_list():
        parse_and_add_bar(get_placeid_infos(res))
        i = i + 1
        print(str(i))


def get_placeid_infos(place_id):
    response = urllib.request.urlopen('https://maps.googleapis.com/maps/api/place/details/json?placeid=' + place_id
                                      + '&key=' + key.gmaps)
    str_response = response.readall().decode('utf-8')

    data = json.loads(str_response)
    response.close()

    return data['result']


def parse_and_add_bar(data):
    try:
        bar_name = data.get('name', 'none')
        bar_address = data.get('formatted_address', 'none')
        bar_coord_lat = data['geometry']['location'].get('lat', 'none')
        bar_coord_lng = data['geometry']['location'].get('lng', 'none')
        bar_phone_nb = data.get('formatted_phone_number', 'none')
        bar_website = data.get('website', 'none')
        bar_gmap_id = data.get('place_id', 'none')
        bar_url_icon = data.get('icon', 'none')
        bar_keywords = ""
        for d in data['types']:
            if bar_keywords == "":
                bar_keywords = bar_keywords + "" + d
            else:
                bar_keywords = bar_keywords + ";" + d

        sqlite_handler.insert_data(bar_name, bar_address, bar_coord_lat, bar_coord_lng, bar_phone_nb, bar_website,
                                   bar_gmap_id, bar_url_icon, bar_keywords)
    except Exception as e:
        print('!. Unable to handle : ' + bar_name + '(' + bar_gmap_id + ')')


def parse_global_list():
    json_data = open('bars_placeid_gapi.json')
    data = json.load(json_data)

    res = []

    for d in data['results']:
        res.append(d['place_id'])

    json_data.close()

    return res


if __name__ == '__main__':
    main()


