#!/usr/bin/env python

def longest_substring(data=None):

    temp = ""
    for i,s in enumerate(data):
        temp += s
        # print temp
        for k,a in enumerate(data):
            if i == k: continue
            # print temp
            if a not in temp:
                temp += a
            elif  len(temp) > len(data[k:]):
                return temp
            else: temp = a
    return temp


# print longest_substring("pwwkew")
print longest_substring("abcabcbb")
print longest_substring("au")
