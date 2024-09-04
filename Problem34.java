public class Problem34 {
    static final int[] factorial = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800};

    static int factorialSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += factorial[num % 10];
            num = num / 10 | 0;
        }

        return sum;
    }

    static void solution() {
        int sum = 0;
        for (int i = 10; i <= 1499999; i++) {
            if (i == factorialSum(i)) 
                sum+= i;
        }

        System.out.println(sum);
    }
    public static void main(String[] args) {
        solution();
    }
}
