"""

Quick sort in place.

"""
import random


x = [random.randint(0, 1000) for x in range(20000)]

def switch(x,i,j):
    x[i] ^= x[j]
    x[j] ^= x[i]
    x[i] ^= x[j]

def quick_sort(x, l, r):

    if l >= r:
        return

    pivot = x[r]
    i = l
    j = r-1
    while i < j:
        if x[i] > pivot and x[j] < pivot:
            switch(x, i, j)
        elif x[i] < pivot:
            i+=1
        elif x[j] > pivot:
            j-=1
        else:
            j-=1
            i+=1

    pivot_index = j if x[j] > pivot else j+1
    switch(x, pivot_index, r) if  r != pivot_index else r
    quick_sort(x, l, pivot_index-1)
    quick_sort(x, pivot_index+1, r)




print('Sorting ', len(x), ' elements')
quick_sort(x, 0, len(x)-1)
