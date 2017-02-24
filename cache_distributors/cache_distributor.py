from enum import Enum

from . import popular_content_distributor
from genetic_distributor import genetic_distributor


class DistributionStrategy(Enum):
    popular_content = 1
    active_endpoints = 2
    genetic = 2

class CacheDistributor():
    @staticmethod
    def distribute(strategy, endpoints, caches, videos):
        distribution = {}
        if strategy == DistributionStrategy.popular_content:
            distribution = popular_content_distributor.distribute(endpoints, caches, videos)
        if strategy == DistributionStrategy.genetic:
            distribution = genetic_distributor.distribute(endpoints, caches, videos)

        return distribution
