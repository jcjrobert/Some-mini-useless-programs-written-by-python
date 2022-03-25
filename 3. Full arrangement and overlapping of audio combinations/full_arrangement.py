import itertools

def full_arrangement(num=4):
    index = [str(i) for i in range(0,num)]
    index_full_arrange = itertools.permutations(index)
    return [''.join(i) for i in index_full_arrange]

# Ensure that each number of the combination is not repeated
def overlay_arrangement(arrange):
    res = []
    num = len(arrange[0])
    temp = []
    while arrange:
        get = arrange[0]
        for i in range(num):
            change = get[1:] + get[0]
            temp.append(change)
            arrange.pop(arrange.index(change))
            get = change
        res.append(temp)
        temp = []
    return res