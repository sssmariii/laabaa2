def solve_sudoku(matrix):
    for r in range(4):
        for c in range(4):
            if matrix[r][c] == 0:
                for num in range(1, 5):
                    if is_valid(matrix, r, c, num):
                        matrix[r][c] = num
                        if solve_sudoku(matrix):
                            return True
                        matrix[r][c] = 0
                return False
    return True

def is_valid(matrix, row, col, num):
    for i in range(4):
        if matrix[row][i] == num:
            return False
        if matrix[i][col] == num:
            return False
            
    start_row = (row // 2) * 2
    start_col = (col // 2) * 2
    for i in range(2):
        for j in range(2):
            if matrix[start_row + i][start_col + j] == num:
                return False
    return True

def main():
    board = [
        [0, 0, 0, 0],
        [0, 0, 2, 0],
        [0, 1, 0, 0],
        [3, 0, 0, 4]
    ]
    
    if solve_sudoku(board):
        for row in board:
            print(row)
    else:
        print("Решения нет")

main()