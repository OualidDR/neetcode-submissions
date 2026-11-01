
def top_k(nums : list, k : int ) -> list  :
    dict = defaultdict(int)
    for n in dict :
        dict[n] += 1
    # return [n, for n, _ in sorted(dict.items(), key= lambda x : -x[1])[:k]]
    return [n for n, _ in sorted(dict.items(), key=lambda x: -x[1])[:k]]
