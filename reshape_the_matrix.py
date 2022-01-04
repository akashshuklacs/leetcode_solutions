class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n= len(mat[0])
        if m*n != r*c:
            return mat
        output_mat = list()
        output_row = list()
        count = 0
        for row in mat:
            for col in row:
                count+=1
                output_row.append(col)
                if count == c:
                    output_mat.append(output_row)
                    output_row = []
                    count = 0
        return output_mat