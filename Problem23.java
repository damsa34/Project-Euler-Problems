import java.util.List;
import java.util.ArrayList;

class Problem23 {

    public static List<Integer> getProperDivisors(int num) {
        List<Integer> properDivisors = new ArrayList<>();
        for (int i = 1; i <= num / 2; i++) {
            if (num % i == 0) properDivisors.add(i);
        }

        return properDivisors;
    }

    public static boolean isAbundant(int num) {
        int sum = 0;
        List<Integer> properDivisors = getProperDivisors(num);

        for (int i = 0; i < properDivisors.size(); i++) {
            sum += properDivisors.get(i);
        }

        return sum > num;
    }

    public static void solution() {
        int sum = 0;
        List<Integer> abundantNumbers = new ArrayList<>();
        for (int i = 12; i <= 28123; i++) {
            if (isAbundant(i)) abundantNumbers.add(i);
        }

        for (int i = 12; i <= 28123; i++) {
            System.out.println("i: " + i + " sum: " + sum);
            for (int j = 12; j <= i; j++) {
                for (int k = 12; k <= i; k++) {
                    if (abundantNumbers.get(i) != abundantNumbers.get(j) + abundantNumbers.get(k))
                        sum += abundantNumbers.get(i);
                    else break;
                }
            }
        }

        System.out.println(sum);
    }
    public static void main (String[] args) {
        solution();
    }
}