public class CountPrimesUpToN {
    public static void main(String[] args) {
        count_primes_up_to_n(12);
    }

    public static void count_primes_up_to_n(int n) {
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                count++;
            }
        }
        System.out.println("There are " + count + " prime numbers up to " + n);
    }

    public static boolean isPrime(int n) { 
        if (n == 1) {
            return false;
        }
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
    
}
