import pygame
import sys

#Create a pre-built Sudoku Board with letters ranging from A-I
def create_board():
    return [
        ["E", "C", "", "", "G", "", "", "", ""],
        ["F", "", "", "A", "I", "E", "", "", ""],
        ["", "I", "H", "", "", "", "", "F", ""],
        ["H", "", "", "", "F", "", "", "", "C"],
        ["D", "", "", "H", "", "C", "", "", "A"],
        ["G", "", "", "", "B", "", "", "", "F"],
        ["", "F", "", "", "", "", "B", "H", ""],
        ["", "", "", "D", "A", "I", "", "", "E"],
        ["", "", "", "", "H", "", "", "G", "I"],
    ]

#Check if letter placement is valid within Sudoku Rules
def is_valid(board, row, col, letter):
#Check row and column for duplicate letters
    for i in range (9):
        if (board[row][i] == letter and i != col) or (board[i][col] == letter and i != row):
            return False 
#Check 3x3 box for duplicate letters
    box_row, box_col = (row // 3) * 3, (col // 3) * 3
    for i in range (3):
        for j in range (3):
            r, c = box_row + i, box_col + j
            if board[r][c] == letter and (r,c) != (row, col):
                return False
    return True


#Check for incorrect letter replacement
def check_board(board):
    incorrect_cells = []
    for row in range(9):
        for col in range(9);
            if board[row][col] != "" and not is_valid(board, row, col, board[row][col]):
                incorrect_cells.append((row, col))
    return incorrect_cells

#Sudoku board with highlighting and error indicators
def draw_board(win, board, selected, incorrect_cells, fixed_cells):
    #Background color white for Sudoku Board
    win.fill((255, 255, 255))
    #Draw Grid Lines
    for i range(10):
        pygame.draw.line(win, (0, 0, 0,), (50 * i, 0), (50 * i, 450), 2)
        pygame.draw.line(win, (0, 0, 0,), (0, 50 * i), (450, 50 * i), 2)

    #Draw letters on the board
    for i range(9):
        for j in range(9):
            if board[i][j] != "":
                font = pygame.font.Font(None, 36)
            #Colors: Pre-filled letters(Black), Incorrect Placement(Red), Player Input(Blue)
            color = (0, 0, 0) if (i, j) in fixed_cells else (225, 0, 0) if (i, j) in incorrect_cells else (0, 0, 225)
            text = font.render(board[i][j], True, color)
            win.blit(text, (j * 50 + 15, i * 50 + 10))
    #Highlights the selected cell
    if selected:
        pygame.draw.rect(win, (0, 255, 0), (selected[1] * 50, selected [0] * 50, 50, 50), 3)
    pygame.display.flip()

#Main Game Loop
def main():
    pygame.init()
    win = pygame.display.set_mode((450, 450))
    pygame.display.set_caption("Sudoku but Letters")
    board = create_board()
    fixed_cells = {(r, c) for r in range(9) for c in range(9) if board[r][c] != ""}
    selected = None
    running = True

    while running
        incorrect_cells = check_board(board) #Checks mistakes
        draw_board(win, board, selected, incorrect_cells, fixed_cells)

        for event in pygame.event.get()
            if event.type == pygame.QUIT:
                running = Flase
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False #Exits game
                elif event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                #Arrow Key Game Navigation
                    if selected:
                        row, col = selected
                        if event.key == pygame.K_UP and row > 0:
                            selected = (row - 1, col)
                        elif event.key == pygame.K_DOWN and row < 8:
                            selected = (row + 1, col)
                        elif event.key == pygame.K_LEFT and col > 0:
                            selected = (row, col - 1)
                        elif event.key == pygame.K_RIGHT < 8:
                            selected = (row, col + 1)
                elif pygame.K_a <= event.key <= pygame.K_i:
                    #Input letters into empty spaces
                    if selected and selected not in fixed_cells:
                        row, col = selected
                        board[row][col] = chr(event.key).upper()
            elif even.type == pygame.MOUSEBUTTONDOWN:
                #Select cell using mouse also
                x, y = event.pos
                selected = (y // 50, x //50)

        #Check if the board is correctly completed
        if len(incorrect_cells) == 0 and all(board[r][c] != "" for r in range(9) for c in range(9)):
            print("Sudoku Letter Puzzle Completed Correctly! Thank you for playing!")
            running = False




