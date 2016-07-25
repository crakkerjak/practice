import java.util.Arrays;

public class insertion_sort {
  public static int[] insertionSort(int[] a) {
    // for each value from 0 to array end
    for (int i = 0; i < a.length; i++) {
      int j = i;
      // move current value left into position in sorted subarray
      int temp = a[j];
      while (j > 0 && a[j - 1] > a[j]) {
        a[j] = a[j - 1];
        a[--j] = temp;
      }
    }
    return a;
  }

  public static void main(String[] args) {
    int[] a = new int[]{10, 9, 8, 3, 4, 5, 2, 1, 0, 11, 12, 2, 7};
    System.out.println(Arrays.toString(insertionSort(a)));
  }
}
