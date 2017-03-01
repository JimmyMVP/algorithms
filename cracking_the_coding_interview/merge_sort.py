import random



x = [random.randint(0, 1000) for x in range(100000)]


def merge(x, y):

    merged = x+y
    i = j = k = 0
    while i < len(x) and j < len(y):

        if x[i] > y[j]:
            merged[k] = y[j]
            j+=1
        else:
            merged[k] = x[i]
            i+=1
        k+=1
    if k != len(merged):
        merged[k:] = x[i:] if i < len(x) else y[j:]

    return merged

def merge_sort(x):

    if len(x) == 2:
        return x if x[0] < x[1] else [x[1], x[0]]
    elif len(x) ==1:
        return x

    left = merge_sort(x[:len(x)//2])
    right = merge_sort(x[len(x)//2+1:])

    min_ind = -1
    max_ind = -1

    return merge(left, right)

print('Sorting ', len(x), ' elements')
merge_sort(x)