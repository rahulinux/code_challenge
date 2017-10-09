#!/usr/bin/env python


def bubble_sort(data):

    sorted = False

    while not sorted:
        sorted = True
        for i in range(0,len(data)-1):
            if data[i] > data[i+1]:
                sorted = False
                data[i+1],data[i] = data[i],data[i+1]
    return data


print bubble_sort([3,4,1])
print bubble_sort([5,9,1,0])
print bubble_sort([0,9,6,8,5,4,3,2,1,7])
print bubble_sort([1,2,3,5,4])
