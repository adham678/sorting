import time
import random
import matplotlib.pyplot as plt


def generate_randomarray(n):
    arr = []
    for i in range(0, n, 1):
        arr.append(random.randint(1, 1000000))
    return arr


def insertion_sort(arr):
    start = time.perf_counter()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end = time.perf_counter()
    print(f"Running time for Insertion Sort with input size {len(arr)} "
          f"is {round((end - start) * 1000, 5)} ms")
    return round((end - start) * 1000, 5)
#--------------------------------------------------------

def bubble_sort(arr):
    start = time.perf_counter()
    n = len(arr)
    for i in range(1, n):
        is_sorted = True
        for j in range(n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted:
            break
    end = time.perf_counter()
    print(f"Running time for Bubble Sort with input size {len(arr)} "
          f"is {round((end - start) * 1000, 5)} ms")
    return round((end - start) * 1000, 5)
#---------------------------------------------------------

def selection_sort(arr):
    start = time.perf_counter()
    n = len(arr)
    for i in range(n - 1):
        min_value = i
        for j in range(i + 1, n):
            if arr[min_value] > arr[j]:
                min_value = j
        arr[i], arr[min_value] = arr[min_value], arr[i]
    end = time.perf_counter()
    print(f"Running time for selection Sort with input size {len(arr)} "
          f" is {round((end - start) * 1000, 5)} ms")
    return round((end - start) * 1000, 5)



def selection_sort_core(arr):
    n = len(arr)
    for i in range(n - 1):
        min_value = i
        for j in range(i + 1, n):
            if arr[min_value] > arr[j]:
                min_value = j
        arr[i], arr[min_value] = arr[min_value], arr[i]

#--------------------------------------------------------------
def partition(arr, low, high):
    r = random.randint(low, high)
    arr[low], arr[r] = arr[r], arr[low]
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while pivot >= arr[i] and i < high:
            i += 1
        while pivot <= arr[j] and j > low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


def quicksort_time(arr):
    start = time.perf_counter()
    quick_sort(arr, 0, len(arr) - 1)
    end = time.perf_counter()
    execution_time_ms = round((end - start) * 1000, 5)
    print(f"Running time for quick Sort with input size {len(arr)} "
          f" {execution_time_ms} ms")
    return execution_time_ms
# -------------------------------heap sort stuf--------------------------------
def max_heapify(arr: list[int], heap_size: int, i: int) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, heap_size, largest)


def build_max_heap(arr: list[int]) -> None:
    heap_size = len(arr)

    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(arr, heap_size, i)


def heap_sort(arr: list[int]) -> float:
    start = time.perf_counter()
    build_max_heap(arr)
    heap_size = len(arr)

    for last in range(len(arr) - 1, 0, -1):
        arr[0], arr[last] = arr[last], arr[0]
        heap_size -= 1
        max_heapify(arr, heap_size, 0)

    end = time.perf_counter()
    execution_time_ms = round((end - start) * 1000, 5)
    print(f"Running time for heap Sort with input size {len(arr)} "
          f" is {execution_time_ms} ms")
    return execution_time_ms

#----------------------------------------------------------------------------------------------------



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result




def mergeSort_time(arr):
    start = time.perf_counter()
    merge_sort(arr)
    end = time.perf_counter()
    execution_time_ms = round((end - start) * 1000, 5)
    print(        f"Running time for merge Sort with input size {len(arr)} "
                      f" {execution_time_ms} ms")
    return execution_time_ms

#---------------------------- hybrid merge + selection sort ----------------------------

def hybrid_merge_sort(arr, threshold):

    if len(arr) <= max(threshold, 1):
        selection_sort_core(arr)
        return arr

    mid = len(arr) // 2

    left = hybrid_merge_sort(arr[:mid], threshold)
    right = hybrid_merge_sort(arr[mid:], threshold)

    return merge(left, right)


def hybrid_sort_time(arr, threshold):
    start = time.perf_counter()
    hybrid_merge_sort(arr, threshold)
    end = time.perf_counter()
    execution_time_ms = round((end - start) * 1000, 5)
    print(f"Running time for hybrid merge-selection Sort with input size {len(arr)} "
          f"(threshold = {threshold}) is {execution_time_ms} ms")
    return execution_time_ms



def main():
    x = [10000, 25000, 50000, 100000]

    arr1 = generate_randomarray(10000)
    arr2 = generate_randomarray(25000)
    arr3 = generate_randomarray(50000)
    arr4 = generate_randomarray(100000)


    y1i = insertion_sort(arr1.copy())
    y2i = insertion_sort(arr2.copy())
    y3i = insertion_sort(arr3.copy())
    y4i = insertion_sort(arr4.copy())
    yi = [y1i, y2i, y3i, y4i]


    y1b = bubble_sort(arr1.copy())
    y2b = bubble_sort(arr2.copy())
    y3b = bubble_sort(arr3.copy())
    y4b = bubble_sort(arr4.copy())
    yb = [y1b, y2b, y3b, y4b]

    y1s = selection_sort(arr1.copy())
    y2s = selection_sort(arr2.copy())
    y3s = selection_sort(arr3.copy())
    y4s = selection_sort(arr4.copy())
    ys = [y1s, y2s, y3s, y4s]

    y1q = quicksort_time(arr1.copy())
    y2q = quicksort_time(arr2.copy())
    y3q = quicksort_time(arr3.copy())
    y4q = quicksort_time(arr4.copy())
    yq = [y1q, y2q, y3q, y4q]

    # Merge sort
    y1m = mergeSort_time(arr1.copy())
    y2m = mergeSort_time(arr2.copy())
    y3m = mergeSort_time(arr3.copy())
    y4m = mergeSort_time(arr4.copy())
    ym = [y1m, y2m, y3m, y4m]

    # Heap sort
    y1h = heap_sort(arr1.copy())
    y2h = heap_sort(arr2.copy())
    y3h = heap_sort(arr3.copy())
    y4h = heap_sort(arr4.copy())
    yh = [y1h, y2h, y3h, y4h]

    # Hybrid merge and selection sort
    threshold = 6
    y1hy = hybrid_sort_time(arr1.copy(), threshold)
    y2hy = hybrid_sort_time(arr2.copy(), threshold)
    y3hy = hybrid_sort_time(arr3.copy(), threshold)
    y4hy = hybrid_sort_time(arr4.copy(), threshold)
    yhy = [y1hy, y2hy, y3hy, y4hy]

    plt.plot(x, yi, label='insertion sort', color='green', linestyle='-', marker='o')
    plt.plot(x, ys, label='selection sort', color='red', linestyle='-', marker='o')
    plt.plot(x, yb, label='bubble sort', color='blue', linestyle='-', marker='o')
    plt.plot(x, yq, label='quick sort', color='purple', linestyle='-', marker='o')
    plt.plot(x, ym, label='merge sort', color='orange', linestyle='-', marker='o')
    plt.plot(x, yh, label='heap sort', color='brown', linestyle='-', marker='o')
    plt.plot(x, yhy, label='hybrid merge-selection sort', color='black', linestyle='-', marker='o')

    plt.grid(True)

    plt.xlabel('input size (N)')
    plt.ylabel('Execution time(ms)')
    plt.title('(example graph)')

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
