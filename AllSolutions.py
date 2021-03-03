# I think it's worth noting how the logical solutions improved as I tried to achieve 100%
###SOLUTION 1###
A = [5, 3, 1, 1, 2, 3, 5, 4]
X = 5
array_len = len(A)
ctr = 0
# check if all elements are in the array
for i in range(1,X+1):
    if i in A:
        ctr += 1
if ctr == X:
    # find the earliest position of each element
    print("all elements complete. frog can cross the river")
    farthest_position = 0
    for j in range(1,X+1):
        element_position = A.index(j)
        print(j)
        print(element_position)
        if element_position > farthest_position:
            farthest_position = element_position
    print(farthest_position)
else:
    print("missing one or more elements. frog cannot cross the river")

###SOLUTION 2###
def solution(X, A):
    # write your code in Python 3.6
    len_array = len(A)
    earliest_time = 0
    element_ctr = 0
    # check if all elements are in the array
    for i in range(1,X+1):
        if i in A:
            element_ctr += 1
    # if all elements are present, find the positions of each element
    if element_ctr == X:
        # determine the earliest time when leaves appear in every position
        for i in range(1,X+1):
            if earliest_time < A.index(i):
                earliest_time = A.index(i)
        return(earliest_time)
    else:        
        earliest_time = -1
        print("A.index(2) = ", A.index(2))
        return(earliest_time)

###SOLUTION 3###
def solution(X, A):
    # write your code in Python 3.6
    earliest_time = 0

    # determine the earliest time when leaves appear in every position
    for i in range(1,X+1):
        try:
            element_position = A.index(i)
        except:
            earliest_time = -1
            return(earliest_time)
        else:
            if earliest_time < element_position:
                earliest_time = element_position
    return(earliest_time)

###SOLUTION 4###
def solution(X, A):
    # write your code in Python 3.6
    len_array = len(A)
    earliest_time = 0
    # determine if the number of leaves is NOT greater than the number of elements
    if X <= len_array:
        # determine the earliest time when leaves appear in every position
        for i in range(1,X+1):
            try:
                element_position = A.index(i)
            except:
                earliest_time = -1
                return(earliest_time)
            else:
                if earliest_time < element_position:
                    earliest_time = element_position
        return(earliest_time)
    # number of leaves is greater than the number of elements; this prevents the unnecessary location of each element
    else:
        earliest_time = -1
        return(earliest_time)

###SOLUTION 5###
def solution(X, A):
    # write your code in Python 3.6
    len_array = len(A)
    earliest_time = 0
    element_position = []
    # determine if the number of leaves is NOT greater than the number of elements
    if X <= len_array:
        # determine the earliest time when leaves appear in every position
        for i in range(1,X+1):
            try:
                element_position.append(A.index(i))
            except:
                earliest_time = -1
                return(earliest_time)
        return(max(element_position))
    # number of leaves is greater than the number of elements; this prevents the unnecessary location of each element when incomplete
    else:
        earliest_time = -1
        return(earliest_time)

###SOLUTION 6###
def solution(X, A):
    # write your code in Python 3.6
    len_array = len(A)
    earliest_time = 0
    # determine if the number of leaves is NOT greater than the number of elements
    if X <= len_array:
        # determine the earliest time when leaves appear in every position
        for i in range(1,X+1):
            try:
                if earliest_time < A.index(i):
                    earliest_time = A.index(i)
            except:
                earliest_time = -1
                return(earliest_time)
        return(earliest_time)
    # number of leaves is greater than the number of elements; this prevents the unnecessary location of each element when incomplete
    else:
        earliest_time = -1
        return(earliest_time)

###SOLUTION 7### (!!!final solution!!!)
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