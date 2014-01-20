import java.util.Arrays;
import java.util.Random;

class Insertion {
    public static void main(String args[]){
        int[] numbers ={4,2,5,8,3,2,9};
        sort(numbers);
        System.out.println(Arrays.toString(numbers));
        test();
    }

    public static void test() {
        int[] numbers;
        Random generator = new Random();
        for (int i = 0; i < 1000; i++) {
            numbers = new int[generator.nextInt(30)];
            for (int j = 0; j < numbers.length; j++) {
                numbers[j] = generator.nextInt(1000);
            }
            sort(numbers);
            for (int j = 1; j < numbers.length; j++) {
                assert numbers[j] >= numbers[j-1];
            }
        }
        System.out.println("All is good");
    }

    public static void sort(int[] num) {
        int i = 0;
        for (int key = 1; key < num.length; key++) {
            i = key;
            while (i > 0 && num[i-1] > num[i]){
                //swap
                num[i] = num[i] ^ num[i-1];
                num[i-1] = num[i] ^ num[i-1];
                num[i] = num[i] ^ num[i-1];
                i--;
            }
        }
    }
}
