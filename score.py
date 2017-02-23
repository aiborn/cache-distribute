
def get_latency(video, endpoint_caches, topology_cache, source_latency):
    for cache_id, latency in endpoint_caches.items():
        videos = topology_cache.get(cache_id, [])
        if video in videos and latency < source_latency:
            source_latency = latency

    return source_latency


def score(endpoints, cache):
    result = 0
    request_count = 0

    for endpoint_id, endpoint in endpoints.items():
        datacenter_latency = endpoint["datacenter_latency"]

        for video, request_count in endpoint["requests"].items():
            request_count += 1
            cache_latency = get_latency(video, endpoint["cache"], cache, datacenter_latency)
            latency = datacenter_latency - cache_latency
            saved_time = request_count * latency
            result += saved_time

    return round((result * 1000) / request_count)

