import argparse
import sys
from random import randrange as rnd


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--output_file', type=str, default='stdout',
                        help='Path to output file(stdout as default)')

    parser.add_argument('--height_of_world', type=int, default=1,
                        help='Height of World(1 as default)')

    parser.add_argument('--width_of_world', type=int, default=1,
                        help='Width of World(1 as default)')

    parser.add_argument('--cells', type=str, default='. # F C',
                        help='All types of cells(\'. # F C\' as default)')

    args = parser.parse_args()

    if args.output_file == 'stdout':
        file = sys.stdout
    else:
        file = open(args.output_file, 'w')

    cells = args.cells.split()

    field = [
        ''.join([cells[rnd(len(cells))] for j in range(args.width_of_world)])
        for i in range(args.height_of_world)]

    for line in field:
        file.write(line + '\n')


if __name__ == '__main__':
    main()
