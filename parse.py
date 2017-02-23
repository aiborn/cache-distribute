import sys

# {
#     endpoint_id: {
#         "datacenter_latency": <datacenter_latency>,
#         "cache": {
#             "cache_id": <latency>,
#         },
#         "requests": {
#             "video_id": <requests_count>
#         }
#     }
# }
def parse(file_path):
    with open(file_path) as file:
        line_args = file.readline().split(' ')
        args = [int(x) for x in line_args]
        [video_cnt, endpoints_cnt, requests, caches_cnt, cache_size] = args

        # parse endpoints
        caches = {}
        for cid in range(caches_cnt):
            caches[cid] = cache_size

        # parse videos sizes
        line_args = file.readline().split(' ')
        videos = [int(x) for x in line_args]

        # parse endpoints
        endpoints = {}
        for endpoint_id in range(endpoints_cnt):
            line = file.readline()
            if line == '':
                # end of file
                break

            # data is related to current endpoint
            [dc_latency, cache_servers] = [int(x) for x in line.split(' ')]
            endpoint = {
                'datacenter_latency': dc_latency,
                'cache': {},
                'requests': {},
            }

            for i in range(cache_servers):
                line = file.readline()
                [cache_id, latency] = [int(x) for x in line.split(' ')]
                endpoint['cache'][cache_id] = latency
            endpoints[endpoint_id] = endpoint
        for req_id in range(requests):
            line = file.readline()
            [video_id, endpoint_id, req_cnt] = [int(x) for x in line.split(' ')]
            endpoints[endpoint_id]['requests'][video_id] = req_cnt

        return [endpoints, caches, videos]

def main():
    if len(sys.argv) < 2:
        print('Need input file')
        exit(1)

    [endpoints, caches, videos_size] = parse(sys.argv[1])
    for eid, e in endpoints.items():
        print(eid, e)
    print(caches)
    print(videos_size)


if __name__ == '__main__':
    print(parse(sys.argv[1]))
    main()
