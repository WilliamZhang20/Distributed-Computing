from dask import delayed
import random

@delayed
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    """Recursive merge sort with delayed evaluation"""
    if len(arr) <= 1:
        return delayed(lambda: arr)()  # Wrap base case in delayed
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # recurse
    right = merge_sort(arr[mid:])  # recurse
    return merge(left, right)

# Example usage
if __name__ == "__main__":
    arr = [random.randint(0, 1000) for _ in range(20)]
    print("Unsorted:", arr)

    sorted_delayed = merge_sort(arr)
    sorted_arr = sorted_delayed.compute()  # Triggers real sorting
    print("Sorted:", sorted_arr)
