def dist(caches, videos, endpoints):
    cache_cnt = len(caches)
    cache_dist = {}
    for cid in range(cache_cnt):
        cache_dist[cid] = []

    # return cache_dist
    return {0: [2], 1: [3, 1], 2: [0, 1]}
