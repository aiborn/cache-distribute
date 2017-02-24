import dist
import parse
import score
import sys
import output


def main():
    input_file = sys.argv[1]
    [endpoints, caches, videos] = parse.parse(input_file)
    out = dist.dist(endpoints, caches, videos)
    clen = 0
    for cid, c in caches.items():
        clen += 1

    output.generate_output(clen, out)


if __name__ == '__main__':
    main()
