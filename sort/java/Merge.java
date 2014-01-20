import java.util.Arrays;

class Merge {
    public static void main(String args[]) {
        int[] numbers = {2, 4, 8, 9, 1, 11, 10};
        System.out.println(Arrays.toString(numbers));
        numbers = sort(numbers);
        System.out.println(Arrays.toString(numbers));
    }

    public static int[] sort(int[] nums) {
        if (nums.length <= 1) {
            return nums;
        }
        int[] left = new int[nums.length/2];
        int[] right = new int[nums.length-left.length];
        System.arraycopy(nums, 0, left, 0, left.length);
        System.arraycopy(nums, nums.length/2, right, 0, right.length);
        left = sort(left);
        right = sort(right);

        // Merge
        int leftPtr = 0;
        int rightPtr = 0;
        int i = 0;
        int[] sorted = new int[nums.length];
        while (leftPtr < left.length || rightPtr < right.length) {
            if (leftPtr >= left.length) {
                sorted[i++] = right[rightPtr++];
            }
            else if (rightPtr >= right.length) {
                sorted[i++] = left[leftPtr++];
            }
            else {
                if (left[leftPtr] < right[rightPtr]) {
                    sorted[i++] = left[leftPtr++];
                }
                else {
                    sorted[i++] = right[rightPtr++];
                }
            }
        }
        return sorted;
    }
}
