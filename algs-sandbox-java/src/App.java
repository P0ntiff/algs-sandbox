public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        StringBuilder helloWorld = new StringBuilder();
        helloWorld.append("Hello World!");
        // reverse the string
        String reversed = helloWorld.reverse().toString();
        System.out.println(reversed);
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
