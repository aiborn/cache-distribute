
def get_latency(video, endpoint_caches, topology_cache, source_latency):
    for cache_id, latency in endpoint_caches.items():
        videos = topology_cache.get(cache_id, [])
        if video in videos and latency < source_latency:
            source_latency = latency

    return source_latency


def score(endpoints, cache):
    result = 0
    total_request_count = 0

    for endpoint_id, endpoint in endpoints.items():
        datacenter_latency = endpoint["datacenter_latency"]

        for video, request_count in endpoint["requests"].items():
            total_request_count += request_count
            cache_latency = get_latency(video, endpoint["cache"], cache, datacenter_latency)
            latency = datacenter_latency - cache_latency
            saved_time = request_count * latency
            result += saved_time

    return round((result * 1000) / total_request_count)

# Debug
# endpoints = {0: {'requests': {1: 1000, 3: 1500, 4: 500}, 'datacenter_latency': 1000, 'cache': {0: 100, 1: 300, 2: 200}}, 1: {'requests': {0: 1000}, 'datacenter_latency': 500, 'cache': {}}}
# result = score(endpoints, {0: [2], 1: [3, 1], 2: [0, 1]})
# print(result)
