from . import entro_py_min
import argparse


# List of the arguments one can use to influence the behavior of the program
parser = argparse.ArgumentParser('entro_py_min', description='Calculate the information entropy of alphabets.')

# INPUT ARGUMENTS
parser.add_argument('strings', nargs='*', default='', type=str, help='Strings to calculate the entropy of.')
parser.add_argument('--files', nargs='*', type=str, default='', help='Provide file path(s) to calculate the entropy of.')

# OUTPUT OPTIONS
parser.add_argument('--simple', nargs='?', type=bool, default=False, help='Determines the explicitness of the output. (True = only entropy shown)')
parser.add_argument('--max', nargs='?', type=bool, default=False, help='Includes the maximum entropy.')

# CONVERT OPTIONS
parser.add_argument('--lower', nargs='?', type=bool, default=False, help='Converts given strings or textfiles to lowercase before calculating.')
parser.add_argument('--upper', nargs='?', type=bool, default=False, help='Converts given strings or textfiles to uppercase before calculating.')
parser.add_argument('--squash', nargs='?', type=bool, default=False, help='Removes all whitespaces before calculating.')
args = parser.parse_args()

# Prepares the queue of different strings
queue = []

# Add all the provided strings to the list
for string in args.strings:
    queue.append(string)

# Add all the provided files to the list
for file in args.files:
    string = entro_py_min.readEntropyFile(file)
    queue.append(string)

# Interates over the collected strings and prints the entropies
for string in queue:
    if args.lower:
        string = string.lower()
    elif args.upper:
        string = string.upper()

    if args.squash:
        string = string.replace(" ", "")

    a, b, c = entro_py_min.calculateEntropy(string)
    entro_py_min.printEntropy(string, a, b, args.simple, (False if not args.max else c))
