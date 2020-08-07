def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for (index, items) in enumerate(a):
        cache[index] = items
    
    for item in a:
        if (item * -1) in cache:
            if item == 0:
                continue
            result.append(-item)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
