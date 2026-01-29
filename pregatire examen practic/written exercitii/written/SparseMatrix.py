class SparseMatrix:
    def __init__(self, row, col):
        self.maxrow = row
        self.maxcol = col
        self.occupied: list[tuple] = []

    def set(self, row, col, val):
        if row >= self.maxrow or col >= self.maxcol:
            raise ValueError
        self.occupied.append((row, col, val))

    def get(self, row, col):
        for pos in self.occupied:
            if pos[0] == row and pos[1] == col:
                return pos[2]
        return None

    def __str__(self):
        printstring = ''
        for row in range(0, self.maxrow):
            for col in range(0, self.maxcol):
                exists = False
                value = None
                for pos in self.occupied:
                    if pos[0] == row and pos[1] == col:
                        exists = True
                        value = pos[2]
                if exists:
                    printstring += f'{value}'
                else:
                    printstring += '0'
                printstring += ' '
            printstring += '\n'
        return printstring

mat = SparseMatrix(3, 3)
mat.set(0, 0, 2)
print(mat)