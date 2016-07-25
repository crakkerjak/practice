import java.util.Arrays;

public class selection_sort{
  public static int[] selectionSort(int[] a) {
    // for each element
    for (int i = 0; i < a.length - 1; i++) {
      // find the minimum remaining value
      int min_index = 0;
      int rest_min = Integer.MAX_VALUE;
      for (int j = i + 1; j < a.length; j++) {
        if (a[j] < rest_min) {
          rest_min = a[j];
          min_index = j;
        }
      }
      // swap if necessary
      if (a[i] > rest_min) {
        int temp = a[i];
        a[i] = a[min_index];
        a[min_index] = temp;
      }
    }
    return a;
  }

  public static void main(String[] args) {
    int[] a = new int[]{10, 9, 8, 3, 4, 5, 2, 1, 0, 11, 12, 2, 7};
    System.out.println(Arrays.toString(selectionSort(a)));
  }
}
