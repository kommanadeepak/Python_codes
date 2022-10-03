# solution to remove an element from list
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # finding number of times the given value present in list.
        # assigning the count to a variable
        count = nums.count(val)
        # iterating through loop till the count to remove the given value from the list.
        for i in range(count):
            nums.remove(val)
        # returning length of the list
        return len(nums)