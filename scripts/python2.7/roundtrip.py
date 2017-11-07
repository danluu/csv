#!/usr/bin/env python2.7

from sys import argv
import csv

with open(argv[1], 'rb') as csv_in:
    reader = csv.reader(csv_in)
    with open(argv[2], 'wb') as csv_out:
        for row in reader:
            writer = csv.writer(csv_out)
            writer.writerow(row)

