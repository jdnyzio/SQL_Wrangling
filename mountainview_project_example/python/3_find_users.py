# %load python/3_find_users.py
#!/usr/bin/env python
import xml.etree.cElementTree as ET
import pprint
import re

from util import logging_itr

"""
This file finds the number of unique users who have contributed to this map.
"""

def get_user(element):
    '''
    Returns the user id associated with the given element.
    '''
    return element.attrib.get('uid')


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if 'uid' in element.attrib:
            if element.attrib['uid'] not in users:
                users.add(element.attrib['uid'])

    return users


if __name__ == "__main__":
    users = process_map('data/mountainview.osm')
    print '{} users contributed'.format(len(users))
