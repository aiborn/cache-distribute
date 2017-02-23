import sys

# list of tuples
# first elem of tuple is cache server, second is list of videos
entities_example = [(0,[2]),
            (1,[3,1]),
            (2,[0,1])]
''' Prints data according to submission file format '''
def generate_output(number_of_servers,entities):
    print(number_of_servers)
    for item in entities:
        string=str(item[0])
        string+=' '
        for i in item[1]:
            string+=str(i)
            string+=' '
        print(string)
