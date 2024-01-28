package primitives;

public class PowerOfTwo {
    public static void main(String[] args) {
        System.out.println("Is 16 a power of two? " + isPowerOfTwo(16));
        System.out.println("Is 7 a power of two? " + isPowerOfTwo(7));
        System.out.println("Is 32 a power of two? " + isPowerOfTwo(32));
        System.out.println("Is 36 a power of two? " + isPowerOfTwo(36));
    }

    public static boolean isPowerOfTwo(int n) { 
        // check if number and'd with bit mask returns exactly zero
        if (n > 0 && (n & (n - 1)) == 0) {
            return true;
        }
        return false;
    }
}
