import sys

from dist import dist
from parse import parse
from score import score
from output import generate_output


def main():
    input_file = sys.argv[1]
    [endpoints, caches, videos] = parse(input_file)

    solution = dist(endpoints, caches, videos)
    result = score(endpoints, solution)

    generate_output(len(caches), solution)

if __name__ == '__main__':
    main()
