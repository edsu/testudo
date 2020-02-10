#!/usr/bin/env python

"""
json2csv.py will read in the individual JSON files that testudo.py writes
and write them out as as single CSV file for processing as a spreadsheet.
"""

import os
import csv
import json

output = csv.writer(open('data/courses.csv', 'w'))
output.writerow([
    'id',
    'title',
    'description',
    'term',
    'department',
    'instructors',
    'seats'
])

for dirpath, dirnames, filenames in os.walk('./data'):
    for filename in filenames:
        if not filename.endswith('.json'):
            continue
        course = json.load(open(dirpath + '/' + filename))
        print(course['id'])
        profs = '; '.join(set([s['instructor'] for s in course['sections']]))
        seats = sum([s['seats'] for s in course['sections']])
        output.writerow([
            course['id'],
            course['title'],
            course['description'],
            course['term'],
            course['department'],
            profs,
            seats,
        ])

