# finding median of two sorted arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1+nums2 # merging two arrays
        nums1.sort()	    # sorting resulted array
        mid = len(nums1)//2 # finding mid index position of resulted array
        # checking length of an array is even or not, based on calculating median of array
        if len(nums1)%2==0: 
            mid = mid-1
            median = (nums1[mid]+nums1[mid+1])/2
        else:
            median = nums1[mid]
        return median       # returning median of two sorted arrays 