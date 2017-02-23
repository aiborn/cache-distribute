
def get_latency(video, endpoint_caches, topology_cache, source_latency):
    for cache_id, latency in endpoint_caches:
        videos = topology_cache[cache_id]
        if video in videos and latency < source_latency:
            source_latency = latency

    return source_latency


def score(topology):
    result = 0
    request_count = 0

    endpoints = topology.endpoints

    for endpoint in endpoints:
        datacenter_latency = endpoint.endpoint.datacenter_latency
        for video, request_count in endpoint.request:
            request_count += 1
            cache_latency = get_latency(video, endpoint.cache, topology.cache)
            latency = datacenter_latency - cache_latency
            saved_time = request_count * latency
            result += saved_time

    return (result * 1000) / request_count

