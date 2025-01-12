import timeit
import random
from Lesson_4_marge_sort_code import merge_sort
from Lesson_4_insertion_sort_code import insertion_sort

arr = 1000
test_arr = [random.randint(1, 10000) for _ in range(arr)]

insertion_execution_time = timeit.timeit(
    lambda: insertion_sort(test_arr), number=10)
insertion_test_result = f"Execution time for insertion sort is {
    insertion_execution_time:.5f} sec."
print(insertion_test_result)

marge_sort_execution_time = timeit.timeit(
    lambda: merge_sort(test_arr), number=10)
marge_sort_test_result = f"Execution time for marge sort is {
    marge_sort_execution_time:.5f} sec."
print(marge_sort_test_result)

timsort_execution_time = timeit.timeit(lambda: sorted(test_arr), number=10)
timsort_test_result = f"Execution time for timesort is {
    timsort_execution_time:.5f} sec."
print(timsort_test_result)
