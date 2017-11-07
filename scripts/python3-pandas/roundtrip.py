#!/usr/bin/env python3

import pandas as pd
import sys


def roundtrip(input_file, output_file):
    df = pd.read_csv(input_file, header=None)
    df.to_csv(output_file, header=False)

if __name__ == "__main__":
    roundtrip(sys.argv[1], sys.argv[2])
