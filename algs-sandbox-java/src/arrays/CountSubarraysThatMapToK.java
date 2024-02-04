package arrays;

import java.util.HashMap;
import java.util.Map;

public class CountSubarraysThatMapToK {
    /**
     * Given an array of unique integers and an integer value k, return the total unique contiguous subarrays that sum to k in the array.

        Input-Output

        Example 1

        Input: [1, 0, -1, 1], k = 0
        Output: 4
        Explanation: 4 subarrays sum up to 0
                        i j  (j inclusive)
        [1, 0, -1, 1]  [1,1]
        [1, 0, -1, 1]  [0,2]
        [1, 0, -1, 1]  [1,3]
        [1, 0, -1, 1]  [2,3]
        Example 2

        Input: [3, 7, -4, -2, 1, 5], k = 3
        Output: 2
        Explanation: 2 subarrays sum up to 3
                            i j  (j inclusive)
        [3, 7, -4, -2, 1, 5]  [0,0]
        [3, 7, -4, -2, 1, 5]  [1,2]

     * 
     * @param args
     */
    public static void main(String[] args) {

    }

    private static int countSubarrays(int arr[], int k) {
        int count = 0;
        Map<Integer, Integer> negatingSumToCounts = new HashMap<>();
        negatingSumToCounts.put(0, 1);
        int runningSum = 0;

        for (int i = 0; i < arr.length; i++) {
            runningSum += arr[i];

            int negatingSumKey = runningSum - k;
            if (negatingSumToCounts.containsKey(negatingSumKey)) {
                count += negatingSumToCounts.get(negatingSumKey);
            }

            negatingSumToCounts.put(runningSum, negatingSumToCounts.getOrDefault(runningSum, 0) + 1);
        }

        return count;
    }
    
}
