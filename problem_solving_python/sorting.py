def merge_sort(input_list, left_index, right_index):
    """
    Merge sort
    """
    if right_index - left_index > 1:
        midpoint = left_index + (right_index - left_index) // 2
        left_sorted = merge_sort(input_list, left_index, midpoint)
        right_sorted = merge_sort(input_list, midpoint, right_index)

        i = 0
        j = 0
        output_list = list()
        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] < right_sorted[j]:
                output_list.append(left_sorted[i])
                i += 1
            else:
                output_list.append(right_sorted[j])
                j += 1

        while i < len(left_sorted):
            output_list.append(left_sorted[i])
            i += 1

        while j < len(right_sorted):
            output_list.append(right_sorted[j])
            j += 1

        return output_list

    else:
        return [input_list[left_index]]

mylist = [12,32, 1, 52, 0, 9, 1]
print("initial list:", mylist)
print("sorted:", merge_sort(mylist, 0, len(mylist)))
