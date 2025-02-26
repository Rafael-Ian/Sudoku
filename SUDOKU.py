import pygame
import sys

#Create a pre-built Sudoku Board with letters ranging from A-I
def create_board():
    return [
        ["E", "C", "", "", "G", "", "", "", ""],
        ["F", "", "", "A", "I", "E", "", "", ""],
        ["", "I", "H", "", "", "", "", "F", ""],
        ["H", "", "", "", "F", "", "", "", "C"],
        ["D", ]
        
        
    ]
#Check if letter placement is valid within Sudoku Rules
#Check row and column for duplicate letters
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
