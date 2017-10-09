#!/usr/bin/env python

def longest_palindromic_substring(data):
    temp = ""
    palindrom_list = []
    start = 0 
    while start <= len(data):
      for i in data[start:]:
          temp += i
          if len(temp) >= 2 and temp == temp[::-1]:
              palindrom_list.append(temp)
      else: temp = ""
      start += 1
    return max(palindrom_list,key=len)



print longest_palindromic_substring("babad")
print longest_palindromic_substring("abxxxxcd")
