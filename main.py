import dist
import parse
import score
import sys


def main():
    input_file = sys.argv[1]
    [endpoints, caches, videos] = parse.parse(input_file)
    out = dist.dist(endpoints, caches, videos)
#     score = score('')


if __name__ == '__main__':
    main()
