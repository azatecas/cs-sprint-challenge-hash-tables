def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    index = {}

    #iterate through weight list
    #if its in the dictionary find its index
    #else put it in the index

    for i in range(length):
        curr_weight = weight[i]
        comp_weight = limit - curr_weight
        if comp_weight in index:
            comp_index = index[comp_weight]
            index_list = [comp_index, i]
            index_list.sort(reverse=True)
            return index_list
        else:
            index[curr_weight] - i

    # return None
