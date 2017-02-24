import sys

from cache_distributors.cache_distributor import CacheDistributor, DistributionStrategy
from parse import parse
from score import score
from output import generate_output


def main():
    input_file = sys.argv[1]
    [endpoints, caches, videos] = parse(input_file)

    #solution = CacheDistributor.distribute(
    #    DistributionStrategy.popular_content,
    #    endpoints,
    #    caches,
    #    videos
    #)

    solution = CacheDistributor.distribute(
        DistributionStrategy.genetic,
        endpoints,
        caches,
        videos
    )

    result = score(endpoints, solution)

    generate_output(len(caches), solution)
    print(result)

if __name__ == '__main__':
    main()
