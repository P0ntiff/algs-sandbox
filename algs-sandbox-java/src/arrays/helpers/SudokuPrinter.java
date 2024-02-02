package arrays.helpers;

public class SudokuPrinter {

    public static void main(String[] args) {
        int numBoards = 3; // Change this number to generate more boards

        int[][][] sudokuBoards = new int[numBoards][][];
        for (int i = 0; i < numBoards; i++) {
            sudokuBoards[i] = SudokuGenerator.generateSudoku();
        }

        System.out.println("Generated Sudoku Boards:");
        for (int i = 0; i < numBoards; i++) {
            System.out.println("Sudoku Board " + (i + 1) + ":");
            SudokuGenerator.printSudokuAsArray(sudokuBoards[i]);
            System.out.println();
        }
    }
}