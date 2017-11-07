#!/usr/bin/env python3

import csv
import sys


def roundtrip(input_file, output_file):
    f_input = open(input_file)
    csvreader = csv.reader(f_input)

    f_output = open(output_file, 'w')
    csvwriter = csv.writer(f_output)

    for row in csvreader:
        csvwriter.writerow(row)


if __name__ == "__main__":
    roundtrip(sys.argv[1], sys.argv[2])
