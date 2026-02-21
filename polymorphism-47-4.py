####Define a class matrix with a member variable row , column and list to hold matrix elements .overload + operator to add two matrix objects

class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.hold = []

    def setMatrix(self):
        for i in range(self.row):
            row_list = []
            for j in range(self.column):
                value = int(input(f"Enter value at row {i} column {j}: "))
                row_list.append(value)
            self.hold.append(row_list)

    def __add__(self, other):
        if self.row != other.row or self.column != other.column:
            print("Matrix addition not possible")
            return None

        result = Matrix(self.row, self.column)

        for i in range(self.row):
            row_list = []
            for j in range(self.column):
                sum_value = self.hold[i][j] + other.hold[i][j]
                row_list.append(sum_value)
            result.hold.append(row_list)

        return result

    def display(self):
        for row in self.hold:
            print(row)
                    
        