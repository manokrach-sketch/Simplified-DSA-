# Also known as the Merge Sort algorithm, this is a divide and conquer algorithm that divides 
# the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
#  The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that 
# assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return sorted(left + right)

numbers = [8, 3, 6, 2]

print(merge_sort(numbers))