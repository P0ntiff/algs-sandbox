package arrays;

import java.util.Map;
import static java.util.Map.entry;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;


class SpiralTraversalMatrix {
    /**
     * Given an mxn matrix, return a spiral readout of its values going clockwise & moving inward layer by layer (starting from the top-left).
        Input-Output

        Example 1

        Input:
        [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
        Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
        Example 2

        Input:
        [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
        ]
        Output: [1, 2, 4, 6, 8, 7, 5, 3]
     */
    public static void main(String[] args) {
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int[][] matrixB = {{1, 2}, {3, 4}, {5, 6}, {7, 8}};
        int[][] singleRow = {{1, 2, 3, 4, 5}};
        int[][] singleCol = {{1}, {2}, {3}, {4}, {5}};

        traverseMatrix(singleCol);
    }

    public static void traverseMatrix(int[][] matrix) {
        // single pointer moving around
        // a 'next' node is either +1, 0 or -1 in each direction

        // if next node is already traversed (or at edge) need to turn right by 90 degrees

        // right is 0, down is 1, bottom is 2, up is 3

        int currentDirection = 0, i = 0, j = 0;
        int rowLength = matrix.length;
        int colLength = matrix[0].length;

        if (rowLength == 1) {
            Arrays.stream(matrix[0]).forEach(x -> System.out.print(x + ", "));
            return;
        } else if (colLength == 1) {
            Arrays.stream(matrix).mapToInt(row -> row[0]).forEach(x -> System.out.print(x + ", "));
            return;
        }

        while (true) {
            int nextRow = getNextRow(currentDirection, i);
            int nextCol = getNextCol(currentDirection, j);

            // exit if already visited node
            if (matrix[i][j] == -1) {       // already visited , exit
                break;
            }

            // visit node
            System.out.print(matrix[i][j] + ", ");
            matrix[i][j] = -1;

            // check if next node is edge or visited, turn if so
            boolean isEdge = ((nextRow >= rowLength || nextRow == -1) || (nextCol >= colLength || nextCol == -1));
            if (isEdge || matrix[nextRow][nextCol] == -1) {
                currentDirection = (currentDirection + 1) % 4;
                nextRow = getNextRow(currentDirection, i);
                nextCol = getNextCol(currentDirection, j);
            }

            // move into next node
            i = nextRow;
            j = nextCol;
        }
    }

    // a 90 degree rotation for the row 
    // -1 becomes 0, 0 becomes 1, 1 becomes 0, 0 becomes -1

    // 90 degree rotation for the col
    // 0 becomes 1, 1 becomes 0, 0 becomes -1, -1 becomes 0


    private static int getNextRow(int direction, int currentRow) {
        Map<Integer, Integer> pointers = Map.ofEntries(
            Map.entry(0, 0),
            Map.entry(1, 1),
            Map.entry(2, 0),
            Map.entry(3, -1)
        );

        return currentRow + pointers.get(direction);
    }

    private static int getNextCol(int direction, int currentCol) {
        Map<Integer, Integer> pointers = Map.ofEntries(
            Map.entry(0, 1),
            Map.entry(1, 0),
            Map.entry(2, -1),
            Map.entry(3, 0)
        );

        return currentCol + pointers.get(direction);
    }
}
