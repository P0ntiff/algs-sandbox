package arrays;

import java.util.stream.IntStream;

public class RotatingA2dMatrix {
    public static void main(String[] args) {
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7 , 8, 9}};
        printMatrix(matrix);
        rotateMatrix(matrix);
        printMatrix(matrix);
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] n: matrix) {
            IntStream.of(n).forEach(x -> System.out.print(x + ","));
            System.out.println("");
        }
    }

    public static void rotateMatrix(int[][] matrix) {
        // 1 2 3        7 4 1
        // 4 5 6.   ->  8 5 2 
        // 7 8 9.       9 6 3

        int size = matrix[0].length - 1;
        int layers = size / 2;
        for (int layer = 0; layer < layers; layer++) {
            for (int i = layer; i < size - layer; i++) {
                int top = matrix[layer][i];
                int right = matrix[i][size - layer];
                int bottom = matrix[size - layer][size - i];
                int left = matrix[size - i][layer];

                matrix[layer][i] = left;
                matrix[i][size - layer] = top;
                matrix[size - layer][size - i] = right;
                matrix[size - i][layer] = bottom;
            }
        }
    }
}
