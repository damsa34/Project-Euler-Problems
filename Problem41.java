import java.util.ArrayList;
import java.util.List;
public class Problem41 {
    public static void main(String[] args) {
        int limit = 1000000;
        int[] notPrime = new int[limit];
        List<Integer> primes = new ArrayList<>();

        notPrime[0] = notPrime[1] = 1;

        for (int i = 2; i < 1000000; i++) {
            if (notPrime[i] == 0)
            primes.add(i);

            for (int j = i * i; j < limit; j += i) {
                notPrime[j] = 1;
            }
                
        }

        int maxSum = 0;
        int maxRun = -1;
        for (int i = 0; i < primes.size(); i++) {
            int sum = 0;
            for (int j = i; j < primes.size(); j++) {
                sum += primes.get(j);
                if (sum > limit) break;
                if (notPrime[sum] == 1 && sum > maxSum && j - i > maxRun) {
                    maxRun = j - i;
                    maxSum = sum;
                }
            }
        }

        System.out.println(maxSum);
    }
}
