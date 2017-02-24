import operator

def dist(endpoints, caches, videos):
    video_requests = {}

    for endpoint_id, endpoint in endpoints.items():
        requests = endpoint["requests"]
        for video, request_count in requests.items():
            if not video_requests.get(video):
                video_requests[video] = 0

            video_requests[video] += request_count

    viral_videos = sorted(video_requests.items(), key=operator.itemgetter(1), reverse=True)
    viral_videos_sizes = [videos[video] for video, requests in viral_videos]

    cache_cnt = len(caches)
    cache_dist = {}

    for cache_id, cache_size in caches.items():
        cache = []
        for video, requests in viral_videos:
            if len(viral_videos_sizes) < video:
                pass

            video_size = viral_videos_sizes[video - 1]

            if cache_size >= video_size:
                cache_size -= video_size
                cache += [video]

        cache_dist[cache_id] = cache

    return cache_dist

