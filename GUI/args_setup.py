import argparse
# Create argument parser
parser = argparse.ArgumentParser(description='Process user input method and perform analysis.')
parser.add_argument('--random', action='store_true', help='Use random parameters for user input')
parser.add_argument('--user', action='store_true', help='Use user-generated parameters for user input', default=True)
parser.add_argument('--la', type=int, metavar='num_tests', help='Perform longitudinal analysis with specified number of tests')
args = parser.parse_args()