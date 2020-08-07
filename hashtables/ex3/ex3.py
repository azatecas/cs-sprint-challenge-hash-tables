def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    index = {}
    result = []
    for i in arrays[0]:
        index[i] = 1
    for i in arrays[1:]:
        for num in i:
            if num in index:
                index[num] += 1
            else:
                index[num] = 1
    for key, value in index.items():
        if value == len(arrays):
            result.append(key)
    
    
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
