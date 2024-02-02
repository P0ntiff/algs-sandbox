package arrays;

import java.util.Arrays;
import java.util.HashSet;

public class ValidSudoku {
    /**
     * Given a 9x9 sudoku board, return true if the board is valid, false otherwise.
        
        Note:

        In sudoku, each row, column, and 3x3 subgrid must contain unique values. A duplicate value in any of these regions invalidates the whole board
        0 denotes an empty cell
     * 
     */
    public static void main(String[] args) {
        int[][] sudokuBoard = {
            {7, 2, 8, 1, 3, 5, 6, 4, 9},
            {6, 9, 5, 4, 2, 7, 8, 3, 1},
            {1, 4, 3, 6, 8, 9, 7, 2, 5},
            {2, 5, 6, 9, 1, 8, 3, 7, 4},
            {3, 8, 1, 2, 7, 4, 9, 5, 6},
            {4, 7, 9, 5, 6, 3, 1, 8, 2},
            {8, 1, 4, 3, 9, 2, 5, 6, 7},
            {9, 3, 2, 7, 5, 6, 4, 1, 8},
            {5, 6, 7, 8, 4, 1, 2, 9, 3}
        };

        System.out.println(isValidWithDictionary(sudokuBoard));
    }

    public static boolean isValidWithDictionary(int[][] board) {
        HashSet<String> seen = new HashSet<>();
        
        for (int i = 0; i < board[0].length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                int boardPos = board[i][j];
                String rowSig = String.format("r_" + i + "_" + boardPos);
                String colSig = String.format("c_" + j + "_" + boardPos);
                String boxSig = String.format("box_" + i / 3 + "_" + j / 3 + "_" + boardPos);

                if (seen.contains(rowSig) || seen.contains(colSig) || seen.contains(boxSig)) {
                    return false;
                } else {
                    seen.addAll(Arrays.asList(rowSig, colSig, boxSig));
                }
            }
        }
        return true;
    }
    
    public static void isValidWithHashes(int[][] board) {
        int[] rowHashes = new int[9];
        int[] colHashes = new int[9];
        // number the subgrids 1->9 from left to right, top to bottom
        int[] subgridHashes = new int[9];

        for (int i = 0; i < board[0].length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                int sig = calculateSignature(board[i][j]);
                rowHashes[i] += sig;
                colHashes[j] += sig;
                subgridHashes[(int)getSubgrid(i, j)] += sig;
            }
        }

        // check if any count is different
    }

    public static double getSubgrid(int i, int j) {
        return Math.floor((i / 3) + 1) * Math.floor((j / 3) + 1) - 1;
    }

    public static int calculateSignature(int n) {
        return (n + 31) * 37;
    }
}
