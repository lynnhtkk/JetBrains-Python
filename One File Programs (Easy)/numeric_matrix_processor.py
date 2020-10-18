# Stage 6/6
# Polished the program
# Added the inverse of a matrix option

import numpy as np

class Matrix:
    result_mat = []
    def __init__(self):
        self.row = 0
        self.col = 0
        self.det = 0


    def get_options(self):
        while True:
            print("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse Matrix
0. Exit""")
            self.opt = input('Your choice: ')
            if self.opt == '0':
                break
            elif self.opt == '1':
                self.sum_matrix()
            elif self.opt == '2':
                self.mult_matrix_constant()
            elif self.opt == '3':
                self.mult_matrix()
            elif self.opt == '4':
                self.transpose_matrix()
            elif self.opt == '5':
                self.get_matrix('')
                self.det = self.det_mat(self.mat)
                print(f'The result is:\n{self.det}')
            elif self.opt == '6':
                self.inverse_mat()
                

        
    def get_matrix(self, order):
        self.row, self.col = map(int, input(f'Enter size of {order} matrix: ').split())
        print(f'Enter {order} matrix:')
        self.mat = [input().split() for _ in range(self.row)]
        
        # Changing type of elements in matrix
        for i in range(self.row):
            for j in range(self.col):
                try:
                    self.mat[i][j] = int(self.mat[i][j])
                except:
                    self.mat[i][j] = float(self.mat[i][j])


    def sum_matrix(self):
        Matrix.result_mat = []
        self.get_matrix('first')
        second = Matrix()
        second.get_matrix('second')
        if self.row != second.row or self.col != second.col:
            print('The operation cannot be performed.\n')
        else:
            for i in range(self.row):
                Matrix.result_mat.append([])
                for j in range(self.col):
                    Matrix.result_mat[i].append(self.mat[i][j] + second.mat[i][j])
            self.format_matrix()


    def mult_matrix_constant(self, num=None, mat=None):
        # if num is None, the function is called seprately.
        # if num is defined, the function is called for inverse_matrix() function
        if not num and not mat:
            self.get_matrix('')
            mat = self.mat.copy()
            num = input('Enter constant: ')
            try:
                num = int(num)
            except:
                num = float(num)
        Matrix.result_mat = [[round(num * mat[i][j], 2) for j in range(self.col)] for i in range(self.row)]     
        self.format_matrix()


    def mult_matrix(self):
        Matrix.result_mat = []
        self.get_matrix('first')
        second = Matrix()
        second.get_matrix('second')
        if self.col != second.row:
            print('The operation cannot be performed.\n')
        else:
            for i in range(self.row):
                Matrix.result_mat.append([])
                for j in range(second.col):
                    temp = 0
                    for k in range(self.col):
                        temp += self.mat[i][k] * second.mat[k][j]
                    Matrix.result_mat[i].append(temp)
        
        self.format_matrix()


    def transpose_matrix(self):
        print("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        toptions = input('Your choice: ')
        if toptions == '1':
            Matrix.result_mat = []
            self.get_matrix('')
            for i in range(self.col):
                Matrix.result_mat.append([])
                for j in range(self.row):
                    Matrix.result_mat[i].append(self.mat[j][i])

            self.format_matrix()
        elif toptions == '2':
            Matrix.result_mat = []
            self.get_matrix('')
            tmp_row = 0
            for i in range(self.col - 1, -1, -1):
                Matrix.result_mat.append([])
                for j in range(self.row - 1, -1, -1):
                    Matrix.result_mat[tmp_row].append(self.mat[j][i])
                tmp_row += 1

            self.format_matrix()
        elif toptions == '3':
            Matrix.result_mat = []
            self.get_matrix('')
            for i in range(self.row):
                Matrix.result_mat.append(self.mat[i][::-1])
            
            self.format_matrix()
        elif toptions == '4':
            self.get_matrix('') 
            Matrix.result_mat = self.mat[::-1]

            self.format_matrix()


    def det_mat(self, mat, total=0):
        indices = list(range(len(mat)))

        # Corner Case 1x1 Matrix
        if len(mat) == 1 and len(mat[0]) == 1:
            return mat[0][0]

        # Base Case
        if len(mat) == 2 and len(mat[0]) == 2:
            val = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
            return val

        for fc in indices:
            #  fc stands for focused column
            copy_mat = mat.copy()
            copy_mat = copy_mat[1:]  # removing first row
            
            #  removing focused column
            for i in range(len(copy_mat)):
                copy_mat[i] = copy_mat[i][0:fc] + copy_mat[i][fc + 1:]

            # Recursive Case
            sub_det = self.det_mat(copy_mat)
            total += ((-1) ** fc) * mat[0][fc] * sub_det

        return total


    def inverse_mat(self):
        self.get_matrix('')
        mat = np.array(self.mat)
        try:
            inv_mat = np.linalg.inv(mat)
            Matrix.result_mat = inv_mat.tolist()
            # Round the elements within matrix
            Matrix.result_mat = [[round(Matrix.result_mat[i][j], 3) for j in range(self.col)] for i in range(self.row)]
            for i in range(self.row):
                for j in range(self.col):
                    if Matrix.result_mat[i][j] == 0:
                        Matrix.result_mat[i][j] = 0
            self.format_matrix()
        except:
            print('This matrix doesn\'t have an inverse.')


    def format_matrix(self):
        # Printing the matrix formattly 
        print('The result is: ')
        for r in Matrix.result_mat:
            print(' '.join(map(str, r)))
        print('')


matrix_a = Matrix()
matrix_a.get_options()
