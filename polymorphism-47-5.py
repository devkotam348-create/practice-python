### in question no 4 , define - operator to subtract two matrix object 

class matrix:
    def __init__(self,rows = None, columns = None):
        self.rows = rows
        self.columns = columns
        self.Matrix = []

    def createMatrix (self):
        for i in range(self.rows):
            row_list = []
            for j in range(self.columns):
                value = int(input(f'Enter the number in the position {i}{j}::'))
                row_list.append(value)
            self.Matrix.append(row_list)

    def __sub__(self,other):
        if self.rows != other.rows or self.columns != other.columns:
            print("Subtraction of provided matrix is not possible")
            return None
        result = matrix(self.rows, self.columns)

        for i in range(self.rows):
            row_list=[]
            for j in range(self.columns):
                value = self.Matrix[i][j] - other.Matrix[i][j]
                row_list.append(value)
            result.Matrix.append(row_list)

        return result
    

    def show(self):
        for row in self.Matrix:
            print(row)


a = matrix(3,3)
b = matrix(3,3)

a.createMatrix()
b.createMatrix()
c = a -b
c.show()

        
        