"""solution to merge the sorted array and assigning it to the first sorted array which is being merged with the second sorted array"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """merging two sorted sub arrays from the given arrays excluding 0 value elements from both the lists and assigning to the third list variable"""   
        nums3 = nums1[:m]+nums2[:n]
        # sorting the third list 
        nums3.sort()
        # clearing the first list to load the the elements of the third list.
        nums1.clear()
        # loading the elements of the third list
        nums1.extend(nums3)