class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __str__(self):
        result = ''
        for mat_row in self.mat:
            for el in mat_row:
                result += str(el) + ' '
            result += '\n'
        return result

    def __add__(self, other):
        res_mat = []
        for row1, row2 in zip(self.mat, other.mat):
            res_row = []
            for el1, el2 in zip(row1, row2):
                res_row.append(el1 + el2)
            res_mat.append(res_row)
        return Matrix(res_mat)


data = Matrix(
    mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
)

data1 = Matrix(
    mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
)

print(data + data1)


