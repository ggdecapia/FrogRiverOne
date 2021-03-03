def solution(X, A):
    # write your code in Python 3.6
    len_array = len(A)
    # check if X is less than the given array length 
    if X <= len_array:
        # eliminate duplicates from A and store into a new array
        A_nodupe = list(dict.fromkeys(A))
        # evaluate if the number of distinct elements = X
        if len(A_nodupe) == X:
            # get the last element value
            last_element = A_nodupe[-1]
            # locate the last_element from the originial array
            earliest_time = A.index(last_element)
        # if at least one element from the given array is missing from the distinct array, return -1
        else:
            earliest_time = -1
        return(earliest_time)
    # if X is greater than the given array length, return -1 
    else:
        earliest_time = -1
        return(earliest_time)