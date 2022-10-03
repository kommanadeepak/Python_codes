# checking whether a number is palindrome or not
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # condition to check whether given integer is negative 
        if(x<0):
            # returning bool value False indicating given integer is not a palindrome.
            return False 
        temp=x
        su=0
        # operation for reversing the given integer
        while(x>0):
            r=x%10
            su=10*su+r
            x=x//10
        # condition to check whether give integer and reverse integer are equal     
        if(temp==su):
            # then returning bool value True indicating given integer is Palindrome
            return True
        else:
            return False # returning False if above condition fails
    
        