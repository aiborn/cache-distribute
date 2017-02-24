import operator

from . import popular_content_distributor
from genetic_algorithm import GeneticAlgorithm
from genetic_distributor import GeneticDistributor


def distribute(endpoints, caches, videos):
    video_requests = {}

    GeneticAlgorithm(GeneticDistributor(lasagna)).run()

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
                continue

            video_size = viral_videos_sizes[video]

            if cache_size >= video_size:
                cache_size -= video_size
                cache += [video]

        cache_dist[cache_id] = cache

    return cache_dist

