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
    return a_list
    

def insertion_sort(a_list):

    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

    a_list[position] = current_value

    end = time.time()
    insertion_sort_time = end - start

    print("The insertion sort function took %10.7f seconds:" % insertion_sort_time)
    return 0


def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        #print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2

    end = time.time()
    shell_time = end - start
    print("The shell function took %10.7f seconds:" % shell_time)
    return shell_time


def gap_insertion_sort(a_list, start, gap):
    for a in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

    return 0


def python_sort(a_list):
    start = time.time()

    sorted_list = a_list.sort()

    end = time.time()
    sort_time = end - start

    print("The sort function took %10.7f seconds:" % sort_time)
    return sort_time

if __name__ == "__main__":

    """Main entry point"""
    insertion_time_total_500 = 0
    insertion_time_total_1000 = 0
    insertion_time_total_5000 = 0

    shell_time_total_500 = 0
    shell_time_total_1000 = 0
    shell_time_total_5000 = 0

    for i in range(100):

        test_list_500 = get_me_random_list(500)
        test_list_1000 = get_me_random_list(1000)
        test_list_5000 = get_me_random_list(5000)

        #sort the list with the python sort function
        python_sort(test_list_500)
        python_sort(test_list_1000)
        python_sort(test_list_5000)


        #after the list has been sorted, calculate the timing
        is_time_500 = insertion_sort(test_list_500)
        insertion_time_total_500 = insertion_time_total_500 + is_time_500

        is_time_1000 = insertion_sort(test_list_1000)
        insertion_time_total_1000 = insertion_time_total_1000 + is_time_1000

        is_time_5000 = insertion_sort(test_list_5000)
        insertion_time_total_5000 = insertion_time_total_5000 + is_time_5000


        #now do a shell list sort
        shell_time_500 = shell_sort(test_list_500)
        shell_time_total_500 = shell_time_total_500 + shell_time_500

        shell_time_1000 = shell_sort(test_list_1000)
        shell_time_total_1000 = shell_time_total_1000 + shell_time_1000

        shell_time_5000 = shell_sort(test_list_5000)
        shell_time_total_5000 = shell_time_total_5000 + shell_time_5000