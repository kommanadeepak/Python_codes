# creating reverse integer from given integer
class Solution:
    def reverse(self, x: int) -> int:
        sum = 0
        flag = 0 
        if x<0:
            flag = 1   # flag indicating it is a negative integer
            x = str(x) # converting into string and seperating negative sign from integer
            temp = int(x[1:]) # converting string to integer
            x = temp
        # operation for reversing an integer    
        while x>0:
            rem = x%10
            sum = sum*10+rem
            x //= 10 
        if flag == 1: # condition to check whether given integer is negative
            sum = int('-'+str(sum)) # concating negative sign to integer  
        if sum >= -2**31 and sum <= 2**31: # checking given integer is in 32-bit range
            return sum  # returning reverse integer
        else:
            return 0    # if above condition is false returning 0