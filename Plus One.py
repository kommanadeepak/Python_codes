# solution to add 1 to the last element of the list
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # assigning -1 to position variable
        pos = -1
        # assigning index value of last element of the list to a variable
        n = len(digits)-1
        temp = n
        # condition to check if last element equals to 9
        if digits[n] == 9:
            """then, operation to find the position of the 9 from which consecutive 9's are present till the last in the list, taking initial position as last index value""" 
            while(n-1 >= 0 and digits[n-1]==9):
                pos = n-1
                n -= 1
            """operation to add 1 to the last element of list and manipulating list according to the   requirement"""    
            if pos > 0:
                digits[pos-1] += 1
                digits[pos:] = [0]*((temp+1)-pos)
            elif pos == 0 or temp == 0:
                if temp == 0:
                    digits[pos:] = [0]*((temp)-pos)
                else:
                    digits[pos:] = [0]*((temp+1)-pos)
                digits = [1]+digits
            else:
                digits[temp-1] += 1
                digits[temp] = 0
        else:
            digits[temp] += 1
        # returning the list after adding 1 to the last element of the list
        return digits   