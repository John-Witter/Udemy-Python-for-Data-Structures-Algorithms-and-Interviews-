def pair_sum(arr, k):
    # create a set of tuples which are current (target, element)
    # create a set of tuples which is ( min(element, seen[target]), max(element, seen[target]) ) ?????
    # iterate through array
    # create a target = k - element
    # if target is not in seen, add to seen (target, element)
    # else add to output tuple (min(element, seen[target]), max(element, seen[target]))

    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            # print(num, 'not in', seen, num not in seen)
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    # print(seen)
    # print(output)
    return len(output)


print(pair_sum([1, 3, 2, 2], 4))  # OUTPUT: 2
