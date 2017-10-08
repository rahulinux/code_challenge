#!/usr/bin/env python


def bubble_sort(data):
    for i,e in enumerate(data):
        for j,k in enumerate(data):
            if i == j: continue
            #if data[j] == data[-1]: break
            if e < k:
                data[i],data[j]=data[j],data[i]
    return data


print bubble_sort([3,4,1])
print bubble_sort([5,9,1,0])
print bubble_sort([0,9,6,8,5,4,3,2,1,7])
