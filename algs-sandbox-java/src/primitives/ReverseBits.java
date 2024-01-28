package primitives;

import java.util.Arrays;

public class ReverseBits {
    public static void main(String[] args) {
        for (int n: Arrays.asList(0b10101010)) {
            System.out.println(n + " reversed is: " + reverseBits(n));
            System.out.println(n + " reversed is: " + reverseBits2(n));
        }
    }

    public static int reverseBits(int n) {
        int output = 0;
        while (n != 0) {
            // peel off each bit, mask with 1
            int bit = n & 1;

            // add to output and shift output left
            output <<= 1;
            output |= bit;

            // shift input right 
            n >>= 1;
        }

        return output;
    }

    public static int reverseBits2(int n) {
        int reversedBits = 0;
        while (n > 0) {
            reversedBits = (reversedBits << 1) | (n & 1);
            n >>= 1;
        }
        return reversedBits;
    }
}
