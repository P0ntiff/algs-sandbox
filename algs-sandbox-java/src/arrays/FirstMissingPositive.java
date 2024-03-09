package arrays;

import java.util.Arrays;

public class FirstMissingPositive {
    /**
     * Given an array of integers nums, return the smallest positive integer not contained in nums.

        Note: 0, though it is an integer, has no sign (it is neither positive nor negative). This reduces to the question asking for the first integer ≥ 1 not in nums.

        Note: The array is not necessarily sorted.

        Input-Output

        Example 1:

        Input: [-3, -2, -1, 0, 1, 3]
        Output: 2

        Example 2:
        Input: [-1, -3, -2]
        Output: 1
     * 
     */
    public static void main(String[] args) {
        int[] input = {-3, -2, -1, 0, 1, 3};
        System.out.println(findFirstMissingPositive(input));
    }

    private static int findFirstMissingPositive(int[] array) {
        // sort array (N * log n) time
        Arrays.sort(array);
        int lastHighest = 0;
        for (int n: array) {
            if (n == lastHighest + 1) {
                lastHighest = n;
            }
        }
        
        return lastHighest + 1;
    }
}