class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[0]*no for no in [val for val in range(1,numRows+1)]]
        for i, row in enumerate(triangle):
            row[0] = 1
            for j, val in enumerate(row[1:-1], start=1):
                row[j] = triangle[i-1][j-1]+triangle[i-1][j]
            row[-1] = 1
        return triangle