#!/usr/bin/env python

def longest_substring(s):
    longest = 0
    start = 0
    visited = [ False for _ in range(256) ]
    for i, char in enumerate(s):
        if visited[ord(char)]:
            while char != s[start]:
                visited[ord(s[start])] = False
                start += 1
            start += 1
        else:
            visited[ord(char)] = True
        longest = max(longest, i - start + 1  )
    return longest

#print longest_substring("pwwkew")
print longest_substring("abcabcbb")
print longest_substring("au")
print longest_substring("aab")
