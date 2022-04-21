def merge_sort(arr):
    if len(arr) < 2:
        return arr       
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged_arr = []
    l = h = 0
    while l < len(left) and h < len(right):
        if left[l] < right[h]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[h])
            h += 1
    merged_arr += left[l:]
    merged_arr += right[h:]
    return merged_arr

merge_sort([6, 5, 3, 1, 8, 7, 2, 4])

