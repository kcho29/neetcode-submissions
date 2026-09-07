class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zerorows = set()
        zerocols = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    zerorows.add(row)
                    zerocols.add(col)
        
        for row in zerorows:
            matrix[row] = [0] * len(matrix[0]) 
        
        for col in zerocols:
            for row in range(len(matrix)):
                # print(row,col, matrix)
                matrix[row][col] = 0
        