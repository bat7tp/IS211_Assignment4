import argparse
# other imports go here

import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    #print(a_list)
    return a_list

    
def sequential_search(a_list, item):
    start = time.time()
    print(float(start))
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    print(float(end))
    ss_time = end-start
    print("Sequential Search took %20.17f:" % ss_time)
    return found, ss_time


def ordered_sequential_search(a_list, item):
    start = time.time()

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

    end = time.time()

    oss_time = end-start
    print("Ordered Sequential Search took %10.7f:" % oss_time)
    return found, oss_time

def binary_search_iterative(a_list, item):
    start = time.time()
    print(float(start))
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

    end = time.time()

    bsi_time = end-start
    print("Binary Search Iterative took %10.7f:" % bsi_time)
    return found, bsi_time

    
def binary_search_recursive(a_list, item):

    if len(a_list) == 0:
        return False

    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)
    return found

if __name__ == "__main__":
    """Main entry point"""
    ss_time_total_500 = 0
    ss_time_total_1000 = 0
    ss_time_total_5000 = 0

    os_time_total_500 = 0
    os_time_total_1000 = 0
    os_time_total_5000 = 0

    bsi_time_total_500 = 0
    bsi_time_total_1000 = 0
    bsi_time_total_5000 = 0

    bsr_time_total_500 = 0
    bsr_time_total_1000 = 0
    bsr_time_total_5000 = 0

    for i in range(100):

        list_test_500 = get_me_random_list(500)
        list_test_1000 = get_me_random_list(1000)
        list_test_5000 = get_me_random_list(5000)


        ss_found, ss_time_results_500 = sequential_search(list_test_500, -1)
        ss_time_total_500 = ss_time_total_500 + ss_time_results_500

        ss_found, ss_time_results_1000 = sequential_search(list_test_1000, -1)
        ss_time_total_1000 = ss_time_total_1000 + ss_time_results_1000

        ss_found, ss_time_results_5000 = sequential_search(list_test_5000, -1)
        ss_time_total_5000 = ss_time_total_5000 + ss_time_results_5000


        os_found, os_time_results_500 = ordered_sequential_search(sorted(list_test_500), 9999999)
        os_time_total_500 = os_time_total_500 + os_time_results_500

        os_found, os_time_results_1000 = ordered_sequential_search(sorted(list_test_1000), 9999999)
        os_time_total_1000 = os_time_total_1000 + os_time_results_1000

        os_found, os_time_results_5000 = ordered_sequential_search(sorted(list_test_5000), 9999999)
        os_time_total_5000 = os_time_total_5000 + os_time_results_5000


        bsi_found, bsi_time_results_500 = binary_search_iterative(sorted(list_test_500), -1)
        bsi_time_total_500 = bsi_time_total_500 + bsi_time_results_500

        bsi_found, bsi_time_results_1000 = binary_search_iterative(sorted(list_test_1000), -1)
        bsi_time_total_1000 = bsi_time_total_1000 + bsi_time_results_1000

        bsi_found, bsi_time_results_5000 = binary_search_iterative(sorted(list_test_5000), -1)
        bsi_time_total_5000 = bsi_time_total_5000 + bsi_time_results_5000

        bsr500_start = time.time()
        bsr_found = binary_search_recursive(sorted(list_test_500), -1)
        bsr500_finish = time.time()
        bsr500_time = bsr500_finish-bsr500_start
        bsr_time_total_500 = bsr_time_total_500 + bsr500_time
        print("Binary Search Recursive took %10.7f:" % bsr500_time)

        bsr1000_start = time.time()
        bsr_found = binary_search_recursive(sorted(list_test_1000), -1)
        bsr1000_finish = time.time()
        bsr1000_time = bsr1000_finish - bsr1000_start
        bsr_time_total_1000 = bsr_time_total_1000 + bsr1000_time
        print("Binary Search Recursive took %10.7f:" % bsr1000_time)

        bsr5000_start = time.time()
        bsr_found = binary_search_recursive(sorted(list_test_5000), -1)
        bsr5000_finish = time.time()
        bsr5000_time = bsr5000_finish - bsr5000_start
        bsr_time_total_5000 = bsr_time_total_5000 + bsr5000_time
        print("Binary Search Recursive took %10.7f:" % bsr5000_time)

    avg_search_time_ss_500 = ss_time_total_500/500
    print(float(avg_search_time_ss_500))

    avg_search_time_ss_1000 = ss_time_total_1000/1000
    print(float(avg_search_time_ss_1000))

    avg_search_time_ss_5000 = ss_time_total_5000 / 5000
    print(float(avg_search_time_ss_5000))


    avg_search_time_oss_500 = os_time_total_500 / 500
    print(float(avg_search_time_oss_500))

    avg_search_time_oss_1000 = os_time_total_1000 / 1000
    print(float(avg_search_time_oss_1000))

    avg_search_time_oss_5000 = os_time_total_5000 / 5000
    print(float(avg_search_time_oss_5000))


    avg_search_time_bsi_500 = bsi_time_total_500 / 500
    print(float(avg_search_time_bsi_500))

    avg_search_time_bsi_1000 = bsi_time_total_1000 / 1000
    print(float(avg_search_time_bsi_1000))

    avg_search_time_bsi_5000 = bsi_time_total_5000 / 5000
    print(float(avg_search_time_bsi_5000))


    avg_search_time_bsr_500 = bsr_time_total_500 / 500
    print(float(avg_search_time_bsr_500))

    avg_search_time_bsr_1000 = bsr_time_total_1000 / 1000
    print(float(avg_search_time_bsr_1000))

    avg_search_time_bsr_5000 = bsr_time_total_5000 / 5000
    print(float(avg_search_time_bsr_5000))
