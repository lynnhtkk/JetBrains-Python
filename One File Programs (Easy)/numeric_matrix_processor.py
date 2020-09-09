# Stage 3/6 of Numeric Matrix Processor
# Include choosing options for the type of operations
# Include Matrix Multiplication by ANOTHER MATRIX

class Matrix:
    result_mat = []
    def __init__(self):
        self.row = 0
        self.col = 0

    def get_options(self):
        while True:
            print('1. Add matrices')
            print('2. Multiply matrix by a constant')
            print('3. Multiply matrices')
            print('0. Exit')
            self.opt = input('Your choice: ')
            if self.opt == '0':
                break
            elif self.opt == '1':
                self.sum_matrix()
            elif self.opt == '2':
                self.mult_matrix_constant()
            elif self.opt == '3':
                self.mult_matrix()
            

    def get_matrix(self, order):
        self.row, self.col = input(f'Enter size of {order} matrix: ').split()
        print(f'Enter {order} matrix:')
        self.mat = [input().split() for _ in range(int(self.row))]

    def sum_matrix(self):
        Matrix.result_mat = []
        self.get_matrix('first')
        second = Matrix()
        second.get_matrix('second')
        if self.row != second.row or self.col != second.col:
            print('The operation cannot be performed.\n')
        else:
            for i in range(int(self.row)):
                Matrix.result_mat.append([])
                for j in range(int(self.col)):
                    Matrix.result_mat[i].append(float(self.mat[i][j]) + float(second.mat[i][j]))
            print('The result is: ')
            for r in Matrix.result_mat:
                print(' '.join(map(str, r)))
            print('')

    def mult_matrix_constant(self):
        self.get_matrix('')
        num = float(input('Enter constant: '))
        Matrix.result_mat = [[num * float(self.mat[i][j]) for j in range(int(self.col))] for i in range(int(self.row))]
        print('The result is: ')
        for r in Matrix.result_mat:
                print(' '.join(map(str, r)))
        print('')

    def mult_matrix(self):
        Matrix.result_mat = []
        self.get_matrix('first')
        second = Matrix()
        second.get_matrix('second')
        if self.col != second.row:
            print('The operation cannot be performed.\n')
        else:
            for i in range(int(self.row)):
                Matrix.result_mat.append([])
                for j in range(int(second.col)):
                    temp = 0
                    for k in range(int(self.col)):
                        temp += float(self.mat[i][k]) * float(second.mat[k][j])
                    Matrix.result_mat[i].append(temp)
        print('The result is: ')
        for r in Matrix.result_mat:
            print(' '.join(map(str, r)))
        print('')

matrix_a = Matrix()
matrix_a.get_options()