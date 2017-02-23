import sys

# map of cache servers and list of videos

# entities_example = {
#     0: [2],
#     1: [3,1],
#     2: [0,1]
# }

''' Prints data according to submission file format '''
def generate_output(number_of_servers,entities):
    print(number_of_servers)
    for k,v in entities.items():
        string=str(k)
        string+=' '
        for i in v:
            string+=str(i)
            string+=' '
        print(string)
