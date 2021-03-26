def inversionCount(a=[], n=0):
    # Your Code Here
    count = 0

    def mergesort(a=[]):
        n = len(a)
        if n <= 1:
            return a
        mid = n // 2
        return merge(mergesort(a[:mid]), mergesort(a[mid:]))

    def merge(arr1=[], arr2=[]):
        nonlocal count
        ans = []
        n, m = len(arr1), len(arr2)
        i1, i2 = 0, 0
        while i1 < n and i2 < m:
            if arr1[0] <= arr2[0]:
                ans.append(arr1.pop(0))
                i1 += 1
            elif arr1[0] > arr2[0]:
                ans.append(arr2.pop(0))
                count += (n - i1)
                i2 += 1
        if i1 == n:
            ans.extend(arr2)
        elif i2 == m:
            ans.extend(arr1)
        return ans

    mergesort(a)
    return count


def mergeSort(arr, n):
    # A temp_arr is created to store
    # sorted array in merge function
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n - 1)


# This Function will use MergeSort to count inversions

def _mergeSort(arr, temp_arr, left, right):
    # A variable inv_count is used to store
    # inversion counts in each recursive call

    inv_count = 0

    # We will make a recursive call if and only if
    # we have more than one elements

    if left < right:
        # mid is calculated to divide the array into two subarrays
        # Floor division is must in case of python

        mid = (left + right) // 2

        # It will calculate inversion
        # counts in the left subarray

        inv_count += _mergeSort(arr, temp_arr,
                                left, mid)

        # It will calculate inversion
        # counts in right subarray

        inv_count += _mergeSort(arr, temp_arr,
                                mid + 1, right)

        # It will merge two subarrays in
        # a sorted subarray

        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count


# This function will merge two subarrays
# in a single sorted subarray
def merge(arr, temp_arr, left, mid, right):
    i = left  # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left  # Starting index of to be sorted subarray
    inv_count = 0

    # Conditions are checked to make sure that
    # i and j don't exceed their
    # subarray limits.

    while i <= mid and j <= right:

        # There will be no inversion if arr[i] <= arr[j]

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    # Copy the remaining elements of left
    # subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    # Copy the remaining elements of right
    # subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count


s = list(map(int,
             "468 335 1 170 225 479 359 463 465 206 146 282 328 462 492 496 443 328 437 392 105 403 154 293 383 422 217 219 396 448 227 272 39 370 413 168 300 36 395 204 312 323".split(
                 ' ')))
s2 = list(map(int,
              "174 165 142 212 254 369 48 145 163 258 38 360 224 242 30 279 317 36 191 343 289 107 41 443 265 149 447 306 391 230 371 351 7 102".split(
                  ' ')))
time = [5, 4, 3, 2, 1] * 100000
print(inversionCount([1, 3, 2, 3, 1], 5), "ANS")
# print(mergeSort(time,len(time)))
