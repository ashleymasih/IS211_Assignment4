import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    timeFinished = time.time() - start_time
    return found, timeFinished


def ordered_sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    timeFinished = time.time() - start_time
    return found, timeFinished


def binary_search_iterative(a_list,item):
    start_time = time.time()
    first = 0

    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
                
    et = time.time()
    timeFinished = et - start_time
    return found, timeFinished
    
    
def binary_search_recursive(a_list,item):
    start_time = time.time()
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            timeFinished = time.time() - start_time
            return True, timeFinished
        else:
            if item < a_list[midpoint]:
                timeFinished = time.time() - start_time
                return binary_search_recursive(a_list[:midpoint], item), timeFinished
            else:
                timeFinished = time.time() - start_time
                return binary_search_recursive(a_list[midpoint + 1:], item), timeFinished
    
    


if __name__ == "__main__":
    """Main entry point"""
    total_time = 0
    for i in range(0, 100):
        mylist = get_me_random_list(500)
        mylist = sorted(mylist)
        check, timeUsed = binary_search_iterative(mylist, 99999999)
        total_time += timeUsed
    for i in range(0, 100):
        mylist = get_me_random_list(1000)
        mylist = sorted(mylist)
        check, timeUsed = binary_search_iterative(mylist, 99999999)
        total_time += timeUsed
    for i in range(0, 100):
        mylist = get_me_random_list(5000)
        mylist = sorted(mylist)
        check, timeUsed = binary_search_iterative(mylist, 99999999)
        total_time += timeUsed
    avg_time = total_time / 300
    print(f"Binary Search Iterative took %10.7f seconds to run, on average" % avg_time)


    total_time = 0
    for i in range(0, 100):
        mylist = get_me_random_list(500)
        # sorting is not needed for sequential search.
        mylist = sorted(mylist)
        check, timeUsed = binary_search_recursive(mylist, 99999999)
        total_time += timeUsed
    for i in range(0, 100):
        mylist = get_me_random_list(1000)
        mylist = sorted(mylist)
        check, timeUsed = binary_search_recursive(mylist, 99999999)
        total_time += timeUsed
    for i in range(0, 100):
        mylist = get_me_random_list(5000)
        mylist = sorted(mylist)
        check, timeUsed = binary_search_recursive(mylist, 99999999)
        total_time += timeUsed
    avg_time = total_time / 300
    print(f"Binary Search Recursive took %10.7f seconds to run, on average" % avg_time)

    total_time = 0
    for i in range(0, 100):
        mylist = get_me_random_list(500)
        check, timeUsed = ordered_sequential_search(mylist, 99999999)
        total_time += timeUsed
    for i in range(0, 100):
        mylist = get_me_random_list(1000)
        mylist = sorted(mylist)
        check, timeUsed = ordered_sequential_search(mylist, 99999999)
        total_time += timeUsed
    for i in range(0, 100):
        mylist = get_me_random_list(5000)
        mylist = sorted(mylist)
        check, timeUsed = ordered_sequential_search(mylist, 99999999)
        total_time += timeUsed
    avg_time = total_time / 300
    print(f"Binary Ordered Sequential Search took %10.7f seconds to run, on average" % avg_time)

    total_time = 0
    for i in range(0, 100):
        mylist = get_me_random_list(500)
        check, timeUsed = sequential_search(mylist, 99999999)
        total_time += timeUsed
    for i in range(0, 100):
        mylist = get_me_random_list(1000)
        mylist = sorted(mylist)
        check, timeUsed = sequential_search(mylist, 99999999)
        total_time += timeUsed
    for i in range(0, 100):
        mylist = get_me_random_list(5000)
        mylist = sorted(mylist)
        check, timeUsed = sequential_search(mylist, 99999999)
        total_time += timeUsed
    avg_time = total_time / 300
    print(f"Binary Sequential Search took %10.7f seconds to run, on average" % avg_time)
