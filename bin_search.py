def binary_search(lst,num, start=0,end=-1):
    if end == -1:
        end = len(lst) -1
    if lst[end] < num:
        return 0
    if lst[start] > num:
        return len(lst)
    if start == end:
        return lst[start] >= num
    elif start == end -1:
        return (lst[start] >= num) + lst[end] >= num
    index = (start+end)/2
    if lst[index] < num:
        return binary_search(lst, num, index, end)
    else: # if lst[index] > num:
        return len(lst[index:]) + binary_search(lst, num, start, index-1)

print binary_search([1,2,3,4,5], 3.5)
print binary_search([1,2,3,4,5], 7)
print binary_search([1,2,3,4,5], 0.5)
