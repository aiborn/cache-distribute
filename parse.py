import sys


def parse(file_path):
    with open(file_path) as file:
        line_args = file.readline().split(' ')
        args = [int(x) for x in line_args]
        [videos, endpoints, requests, caches, cache_size] = args

        line_args = file.readline().split(' ')
        videos_size = [int(x) for x in line_args]

        endpoints = []
        for 
        return {
            'video': videos_size,
            'endpoints': [{
                'id': endpoint_id,
                'datacenter_latency': data_center_latency,
                'cache': {
                    'cache_id': latency,
                },
                'requests': {
                    'video_id': requests_count
                }
            }]
        }

def main():
    if len(sys.argv) < 2:
        print('Need input file')
        exit(1)

    parse(sys.argv[1])


if __name__ == '__main__':
    main()
