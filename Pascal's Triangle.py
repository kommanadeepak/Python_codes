# solution to create pascal's triangle from the given numRows value indicating number of rows
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # creating an empty list
        list1 = []
        """creating lists of list with first and last elements of the inner lists as 1 and remaining values as 0"""
        for i in range(1,numRows+1):
            list2 = [1]
            for j in range(2,i+1):
                if j < i:
                    list2.append(0)
                else:
                    list2.append(1)
            list1.append(list2)
            """changing 0 values of the inner lists to the values present in the Pascal's triangle""" 
            for i in range(1,len(list1)):
                for j in range(1,len(list1[i-1])):
                    list1[i][j] = list1[i-1][j-1]+list1[i-1][j]
        # returning the list representing Pascal's triangle            
        return list1