package arrays;

import java.util.ArrayList;
import java.util.List;

public class EnumeratePrimesToN {
    /**
     * Given a non-negative integer n, return a list enumerating all prime numbers < n.

        Input-Output

        Example 1

        Input: 1
        Output: []
        Explanation: 1 is not a prime number
        Example 2

        Input: 31
        Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

     * 
     */
    public static void main(String[] args) {
        int n = 31;
        List<Integer> output = enumerateAllPrimesToN(n);
        output.stream().forEach(x -> System.out.print(x + ", "));
    }

    public static List<Integer> enumerateAllPrimesToN(int n) {
        // Avoid repeat work, forward eliminate multiples of the numbers that are found to be prime
        boolean[] isPrime = new boolean[n];
        List<Integer> output = new ArrayList<>();
        for (int i = 0; i < n; i++) { 
            isPrime[i] = true;
        } 

        isPrime[0] = false;
        isPrime[1] = false;

        for (int i = 0; i < n; i++) {
            if (isPrime[i]) {
                for (int j = i + i; j < n; j += i) {
                    isPrime[j] = false;;
                }

                output.add(i);
            }    
        }
        return output;
    }
}
