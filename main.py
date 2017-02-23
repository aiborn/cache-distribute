import dist
import parse
from score import score
import sys


def main():
    input_file = sys.argv[1]
    [endpoints, caches, videos] = parse.parse(input_file)
    solution = dist.dist(endpoints, caches, videos)
    result = score(endpoints, solution)

    print(result)


if __name__ == '__main__':
    main()
