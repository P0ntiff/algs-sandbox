package primitives;

import java.util.Arrays;
import java.util.stream.IntStream;

public class PowerOfFour {
    public static void main(String[] args) {
        for (int n : IntStream.of(1, 4, 16, 64).toArray()) {
            System.out.println("Is " + n + " a power of four? " + isPowerOfFour(n));
        }
        for (int n : Arrays.asList(1, 2, 5, 8, 32, 66)) {
            System.out.println("Is " + n + " a power of four? " + isPowerOfFour(n));
        }
    }

    public static boolean isPowerOfFour(int n) {
        // must be a power of two (only one digit set)
        boolean hasSingleLeadingOneBit = (n & (n - 1)) == 0;

        // must fall onto an odd position (one of every second digit)
        boolean hasOddPositionBits = (n & 0b0101010101010101) == n;

        return n != 0 && hasSingleLeadingOneBit && hasOddPositionBits;
    }
}
