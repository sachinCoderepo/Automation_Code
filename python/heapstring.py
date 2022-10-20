import heapq as hq

class Node:
    key=None
    val=None
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __repr__(self):
        return f'Node value: {self.val}'


def get_frequency(string):
    dict1 = {}
    for i in str:
        if i in dict1:
            dict1[i] = dict1.get(i)+1
        else:
            dict1[i] = 1

    return dict1

def get_list_of_objects(freq_dict):
    my_list = []
    for k,v in freq_dict.items():
        node = Node(k,v)
        my_list.append(node)
    return my_list

def my_print(list):
        while len(list) >0:
            o = hq.heappop(list)
            print("key: {0} {1}".format(o.key, o.val))

if __name__ == "__main__":
    str = "ccmbaaabebbbbecc"
    freq_dict = get_frequency(str)
    my_list = get_list_of_objects(freq_dict)
    hq.heapify(my_list)
    my_print(my_list)
    
