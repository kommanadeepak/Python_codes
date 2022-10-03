# solution to insert search position of target to list.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # condition to check if target present in nums
        if target in nums:
            # then accessing index value of target from list and assigning to a variable
            position = nums.index(target)
        # if target is not in list    
        else:
            # inserting the target in the middle of the list.
            # to reduce the time complexity while inserting, better to insert in the middle
            # rather than inserting first or last to the list.
            nums.insert(len(nums)//2,target)
            # sorting the list
            nums.sort()
            # accessing index value of the target from the list and assigning to a variable
            position = nums.index(target)
        return position # returning index value of target present in the list