public class Problem47 {
    private static int countDistinctPrimeFactors(int n) {
        int count = 0;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                do n /= i;
                while (n % i == 0);
                count++;
            }
        }

        if (n > 1) count++;
        return count;
    }

    private static boolean hasFourPrimeFactors(int n) {
        return countDistinctPrimeFactors(n) == 4;
    }

    private static String solution() {
        for (int i = 2;; i++) {
            if (hasFourPrimeFactors(i) &&
                hasFourPrimeFactors(i + 1) &&
                hasFourPrimeFactors(i + 2) &&
                hasFourPrimeFactors(i + 3)) return Integer.toString(i);
        }
    }
    public static void main(String[] args) {
        System.out.println(solution());
    }
}
