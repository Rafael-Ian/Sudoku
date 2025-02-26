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
    for i in range (3)
    
#Check for incorrect letter replacement
#Background color white for Sudoku Board
#Draw Grid Lines
#Draw letters on the board
#Colors: Pre-filled letters(Black), Incorrect Placement(Red), Player Input(Blue)
#Highlight selected cell
#Game Loop
#Check mistakes
#Arrow Key Game Navigation
#Select cell using mouse also
#Check if the board is correctly completed
#
