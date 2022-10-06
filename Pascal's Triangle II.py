# solution to get rowIndexed element of Pascal's Triangle
def getRow(self, rowIndex: int) -> List[int]:
        # taking an empty list
        list1 = []
        """creating elements of pascal's triangle with first and
           last elements as 1 and remaining elements as 0"""
        for i in range(0, rowIndex+1):
            list2 = [1]
            for j in range(1, i+1):
                if j < i:
                    list2.append(0)
                else:
                    list2.append(1)
            list1.append(list2)
        """replacing 0 elements with appropriate element of pascal's triangle"""
        for i in range(1, len(list1)):
            for j in range(1,i):
                list1[i][j] = list1[i-1][j-1]+list1[i-1][j]
        # returning particular rowIndexed element of pascal's triangle
        return list1[rowIndex]