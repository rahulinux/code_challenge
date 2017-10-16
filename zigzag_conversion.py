#!/usr/bin/env python



def zigzag_conversion(s,n):
       d = {}
       a = 0
       d[a] = []
       for i in range(len(s)):
           if len(d[a]) == n:
               a += 1
               d[a] = [s[i]]
               a += 1
               d[a] = []
           else:
              d[a] += [s[i]]
       return ''.join([ ''.join(d[i]) for i in d])



print zigzag_conversion("PAYPALISHIRING",3)
