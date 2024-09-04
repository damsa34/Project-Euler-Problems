public class Problem37 {
    static boolean isPrime(int num) {
        if (num <= 1) return false; 
        
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }

        return true;
    }

    static boolean isTruncatablePrime(int num) {
        for (int i = 10; i < num; i *= 10) {
            if (!isPrime(num % i) || !isPrime(num / i | 0)) return false;
        }

        return true;
    }

    static void solution() {
        int sum = 0;
        for (int i = 1; i <= 1000000; i++) {
            System.out.println(i);
            if (isTruncatablePrime(i)) sum += i;
        }

        System.out.println("Sum: " + sum);
    }
    public static void main(String[] args) {
        solution();
    }
}
