package primitives;

import java.util.Arrays;

public class Palindrome {
    public static void main(String[] args) {
        for (int n: Arrays.asList(12321, 456654)) {
            System.out.println("Is " + n + " a palindrome? " + isPalindrome(n));
        }
    }

    public static boolean isPalindrome(int n) {
        int totalDigits = (int) Math.floor(Math.log10(n)) + 1;
        int msdMask = (int) Math.pow(10, totalDigits - 1);

        for (int i = 0; i < (totalDigits / 2); i++) {
            // extract most and least significant digits
            int lsd = n % 10;
            int msd = n / msdMask;

            if (msd != lsd) {
                return false;
            }
            
            // peel off digits
            n %= msdMask;
            n /= 10;

            msdMask /= 100;
        }
        return true;
    }
}
