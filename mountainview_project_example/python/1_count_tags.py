# %load python/1_count_tags.py
#!/usr/bin/env python
"""
This file counts how many of each tag is present in the given XML file.
"""
import xml.etree.cElementTree as ET
import pprint

from collections import defaultdict
from util import logging_itr

def count_tags(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    tags = {}
    for child in root:
        tag = child.tag
        if tag not in tags:
            tags[tag] = 1
        else:
            tags[tag] = tags[tag]+1
    return tags

if __name__ == "__main__":
    tags = count_tags('data/mountainview.osm')
    pprint.pprint(tags)
    
