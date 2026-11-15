class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [sum(r) for r in mat]
        cols = [sum(c) for c in zip(*mat)]

        return sum(
            mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1
            for i in range(len(mat))
            for j in range(len(mat[0]))
        )