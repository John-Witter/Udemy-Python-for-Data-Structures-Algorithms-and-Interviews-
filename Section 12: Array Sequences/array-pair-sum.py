def pair_sum(arr, k):

    seen = set()
    output = set()

    for num in arr:
        target = k - num
        print('num:', num, 'target:', target)
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    print(seen)
    return output


print(pair_sum([1, 3, 2, 2], 4))  # OUTPUT: 2
