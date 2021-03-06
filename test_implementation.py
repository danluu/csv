#!/usr/bin/env python3

import glob
import os
import sys


def create_output_csvs(original_csvfile, output_csvfile, script_location):
        os.system("{} {} {}".format(script_location, original_csvfile, output_csvfile))
        os.system("diff {} {}".format(original_csvfile, output_csvfile))


if __name__ == "__main__":
    project_name = sys.argv[1]
    script_location = glob.glob("scripts/{}/*".format(project_name))[0]

    original_csvfiles = glob.glob('fixtures/*.csv')

    output_csvfiles = [os.path.abspath("output-{}-{}".format(project_name, file)) for file in original_csvfiles]
    original_csvfiles = [os.path.abspath(file) for file in original_csvfiles]

    # make sure the directory for output exists
    os.makedirs(os.path.dirname(output_csvfiles[0]), exist_ok=True)

    files = zip(original_csvfiles, output_csvfiles)

    for original_csvfile, output_csvfile in files:
        create_output_csvs(original_csvfile, output_csvfile, script_location)
