import heapq as hq

def get_frequency(string):
    dict1 = {}
    for i in string:
        if i in dict1:
            dict1[i] = dict1.get(i)+1
        else:
            dict1[i] = 1

    return dict1

def sort_by_frq():
    str = "ccmbaaabebbbbecc"
    freq_dict = get_frequency(str)

    freq_tuple_list = [(val*-1, key) for  val,key in freq_dict.items()]
    hq.heapify(freq_tuple_list)

    while len(freq_tuple_list) > 0:
        i = hq.heappop(freq_tuple_list)
        # print("key: {1} value: {0}".format(i[0]*-1, i[1]))
        print(f"key: {i[0]*-1} value: {i[1]}")

sort_by_frq()
