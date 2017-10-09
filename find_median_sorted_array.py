class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def bubble_sort(data=[]):
            sorted = False
            while not sorted:
                sorted = True
                for i in range(0,len(data)-1):
                    if data[i] > data[i+1]:
                        sorted = False
                        data[i],data[i+1] = data[i+1],data[i]
            return data
        
        #l = bubble_sort(nums1 + nums2)
        l = sorted(nums1 + nums2)
        # if input list is even
        if len(l)%2 == 0:
            m = len(l)//2
            a,b = l[m-1],l[m]
            median = (a+b)/2.0
        else:
            m = int(len(l)//2)
            median = l[m]
        return median
