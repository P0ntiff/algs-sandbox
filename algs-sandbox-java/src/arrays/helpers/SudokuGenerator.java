package arrays.helpers;

import java.util.Random;

public class SudokuGenerator {

    public static void main(String[] args) {
        int[][] sudokuBoard = generateSudoku();
        printSudoku(sudokuBoard);
    }

    public static int[][] generateSudoku() {
        int[][] board = new int[9][9];
        fillDiagonalSubgrids(board);
        solveSudoku(board);
        return board;
    }

    public static void fillDiagonalSubgrids(int[][] board) {
        Random random = new Random();
        for (int i = 0; i < 9; i += 3) {
            fillSubgrid(board, i, i);
        }
    }

    public static void fillSubgrid(int[][] board, int startRow, int startCol) {
        Random random = new Random();
        int[] nums = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        shuffleArray(nums);

        int index = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[startRow + i][startCol + j] = nums[index++];
            }
        }
    }

    public static void shuffleArray(int[] array) {
        Random random = new Random();
        for (int i = array.length - 1; i > 0; i--) {
            int index = random.nextInt(i + 1);
            int temp = array[index];
            array[index] = array[i];
            array[i] = temp;
        }
    }

    public static boolean solveSudoku(int[][] board) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                if (board[row][col] == 0) {
                    for (int num = 1; num <= 9; num++) {
                        if (isValidMove(board, row, col, num)) {
                            board[row][col] = num;
                            if (solveSudoku(board)) {
                                return true;
                            }
                            board[row][col] = 0; // Backtrack
                        }
                    }
                    return false; // No valid number for this cell
                }
            }
        }
        return true; // All cells filled successfully
    }

    public static boolean isValidMove(int[][] board, int row, int col, int num) {
        return !usedInRow(board, row, num) && !usedInColumn(board, col, num) && !usedInSubgrid(board, row - row % 3, col - col % 3, num);
    }

    public static boolean usedInRow(int[][] board, int row, int num) {
        for (int col = 0; col < 9; col++) {
            if (board[row][col] == num) {
                return true;
            }
        }
        return false;
    }

    public static boolean usedInColumn(int[][] board, int col, int num) {
        for (int row = 0; row < 9; row++) {
            if (board[row][col] == num) {
                return true;
            }
        }
        return false;
    }

    public static boolean usedInSubgrid(int[][] board, int startRow, int startCol, int num) {
        for (int row = 0; row < 3; row++) {
            for (int col = 0; col < 3; col++) {
                if (board[startRow + row][startCol + col] == num) {
                    return true;
                }
            }
        }
        return false;
    }

    public static void printSudoku(int[][] board) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                System.out.print(board[row][col] + " ");
            }
            System.out.println();
        }
    }
    
    public static void printSudokuAsArray(int[][] board) {
        System.out.println("{");
        for (int row = 0; row < 9; row++) {
            System.out.print("  {");
            for (int col = 0; col < 9; col++) {
                System.out.print(board[row][col]);
                if (col < 8) {
                    System.out.print(", ");
                }
            }
            System.out.print("}");
            if (row < 8) {
                System.out.println(",");
            } else {
                System.out.println();
            }
        }
        System.out.println("}");
    }
}
