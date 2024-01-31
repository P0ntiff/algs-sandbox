package arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

/**
 * 
    Given an array of integers, return all unique triplets [a, b, c] (where a ≤ b ≤ c) in the array such that a + b + c = 0. If no such triplets exist return an empty array/list.
    Input-Output

    Example 1

    Input: [-3, -1, 1, 0, 2, 10, -2, 8]
    Output:
    [
    [-3, 1, 2],
    [-2, 0, 2],
    [-1, 0, 1]
    ]

    Example 2

    Input: [-5, 3, 2, 0, 1, -1, -5, 3, 2]
    Output:
    [
    [-5, 2, 3],  # the same triplet is not duplicated
    [-1, 0, 1]
    ]
 */
public class ThreeSum {
    public static void main(String[] args) {
        int[] array = {-3, -1, 1, 0, 2, 10, -2, 8};
        Arrays.asList(array).forEach(System.out::print);
        ArrayList<List<Integer>> result = findThreeSums(array);
        for (var triple : result) {
            System.out.println(triple);
        }
    }

    public static ArrayList<List<Integer>> findThreeSums(int[] array) {
        Arrays.sort(array);
        HashSet<List<Integer>> threeSums = new HashSet<>();
        if (array.length < 3) {
            return new ArrayList<>();
        }
        for (int i = 0; i < array.length - 2; i++) {
            findThreeSum(i, array, threeSums);
        }
        return new ArrayList<>(threeSums);
    }

    public static void findThreeSum(int rootIndex, int[] array, HashSet<List<Integer>> result) {
        int left = rootIndex + 1, right = array.length - 1;
        while (left < right) {
            int threeSum = array[rootIndex] + array[left] + array[right];
            if (threeSum > 0) {
                right--;
            } else if (threeSum < 0) {
                left++;
            } else {
                result.add(Arrays.asList(array[rootIndex], array[left++], array[right--]));
            }
        }        
    }
}
