# Stage 3/6 of Numeric Matrix Processor
# Include choosing options for the type of operations
# Include Matrix Multiplication by ANOTHER MATRIX
# Added Transpose Option

class Matrix:
    result_mat = []
    def __init__(self):
        self.row = 0
        self.col = 0

    def get_options(self):
        while True:
            print("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
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
            

    def get_matrix(self, order):
        self.row, self.col = map(int, input(f'Enter size of {order} matrix: ').split())
        print(f'Enter {order} matrix:')
        self.mat = [input().split() for _ in range(self.row)]

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
                    Matrix.result_mat[i].append(float(self.mat[i][j]) + float(second.mat[i][j]))
            
            self.format_matrix()

    def mult_matrix_constant(self):
        self.get_matrix('')
        num = float(input('Enter constant: '))
        Matrix.result_mat = [[num * float(self.mat[i][j]) for j in range(int(self.col))] for i in range(int(self.row))]
        
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
                        temp += float(self.mat[i][k]) * float(second.mat[k][j])
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

    def format_matrix(self):
        print('The result is: ')
        for r in Matrix.result_mat:
            print(' '.join(map(str, r)))
        print('')


matrix_a = Matrix()
matrix_a.get_options()