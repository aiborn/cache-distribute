import operator

def sort_by_total_req(endpoints):
    total = []
    for eid, e in endpoints.items():
        total_r = 0
        requests = e['requests']
        for rid, rcnt in requests.items():
            total_r += rcnt
        total.append((eid, total_r))

    tmp = sorted(total, key=lambda t: t[1], reverse=True)
    return tmp


def sort_request_desc(videos):
    tmp = sorted(videos.items(), key=operator.itemgetter(1), reverse=True)
    return tmp


def sort_latency_asc(caches):
    tmp = sorted(caches.items(), key=operator.itemgetter(1))
    return tmp


# caches <id, size>
# videos <id, size>
def dist(endpoints, caches, videos):
    # this algorithm tries to maximaze the requests
    # sent from endpoints and also tries to mimimaze
    # the latency in a greedy way
    caches_dist = {}

    # Sort endpoints descending by total requests. The endpoints with
    # most total requests come first
    total_requests = sort_by_total_req(endpoints)
    for eid, total_req in total_requests:
        # For each endpoint sort its requests count descending.
        # Vidoes with biggest request count come first.
        endpoint = endpoints[eid]
        videos_req = sort_request_desc(endpoint['requests'])

        # Sort the caches to which the endpoint is connected
        # by latency in ascending order. Caches with lowest latency
        # come first.
        caches_latency = sort_latency_asc(endpoint['cache'])

        # Fill the caches with lowest latency with the videos
        # with most request to them which can be stored
        # in the cache (due to cache size limitations)
        for cid, clat in caches_latency:
            if cid not in caches_dist:
                caches_dist[cid] = []

            for vid, vreq in videos_req:
                if vid in videos:
                    if caches[cid] > videos[vid]:
                        caches[cid] -= videos[vid]
                        caches_dist[cid].append(vid)
                        del videos[vid]
    return caches_dist
