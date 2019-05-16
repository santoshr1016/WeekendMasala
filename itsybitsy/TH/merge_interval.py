def merge_intervals(intervals):
    """
    A simple algorithm can be used:
    1. Sort the tuples in increasing order, key[0]
    2. Push the first tuple on the stack
    3. Iterate through tuples and for each one compare current tuple[0]
       with the top of the stack[1] and:
       A. If current tuple does not overlap, push on to stack
       B. If current tuple overlaps, merge both intervals in to one
          and push on to stack
    4. At the end return stack
    """
    si = sorted(intervals, key=lambda tup: tup[0])
    print(si)
    merged = []

    for tup in si:
        if not merged:
            merged.append(tup)
        else:
            b = merged.pop()
            if b[1] >= tup[0]:
                new_tup = tuple([b[0], tup[1]])
                merged.append(new_tup)
            else:
                merged.append(b)
                merged.append(tup)
    return merged

if __name__ == '__main__':

    l = [(5, 7), (11, 116), (3, 4), (10, 12), (6, 12)]
    print("Original list of ranges: {}".format(l))
    merged_list = merge_intervals(l)
    print("List of ranges after merge_ranges: {}".format(merged_list))