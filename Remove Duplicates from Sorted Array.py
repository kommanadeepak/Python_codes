# solution to remove duplicate values from sorted array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # converting given list into set and assigning to a variable.
        # set does not contain duplicate values.
        a = list(set(nums))
        # emptying the list
        nums.clear()
        # loading elements of set into list
        for i in a:
            nums.append(i)
        # sorting the list    
        nums.sort()
        # returning the length of the list
        return len(nums)