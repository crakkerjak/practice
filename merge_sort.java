import java.util.LinkedList;
import java.util.Arrays;

public class merge_sort {
  private static LinkedList<Integer> merge(LinkedList<Integer> l1,
      LinkedList<Integer> l2) {
    LinkedList<Integer> merged_list = new LinkedList<Integer>();
    // merge lists (assumed ordered) until one is empty
    while (l1.size() > 0 && l2.size() > 0)
      if (l1.peek() < l2.peek())
        merged_list.add(l1.pop());
      else
        merged_list.add(l2.pop());
    // append remaining elements
    merged_list.addAll(l1);
    merged_list.addAll(l2);

    return merged_list;
  }


  public static LinkedList<Integer> mergeSort(LinkedList<Integer> l) {
    // base case
    if (l.size() < 2) return l;
    // split list in two
    LinkedList<Integer> l2 = new LinkedList<Integer>();
    for (int i = 0; i < l.size() / 2; i++)
      l2.add(l.pop());
    // recurse on both halves
    return merge(mergeSort(l), mergeSort(l2));
  }


  private static int[] merge(int[] a1, int[] a2) {
    int[] merged_array = new int[a1.length + a2.length];
    int i1 = 0, i2 = 0;
    // merge (sorted) arrays until one is completely copied
    while (i1 < a1.length && i2 < a2.length)
      if (a1[i1] < a2[i2])
        merged_array[i1 + i2] = a1[i1++];
      else
        merged_array[i1 + i2] = a2[i2++];
    // copy over the rest
    while (i1 < a1.length)
      merged_array[i1 + i2] = a1[i1++];
    while (i2 < a2.length)
      merged_array[i1 + i2] = a2[i2++];

    return merged_array;
  }

  public static int[] mergeSort(int[] a) {
    // base case
    if (a.length < 2) return a;
    // recurse on two array halves
    return merge(mergeSort(Arrays.copyOfRange(a, 0, a.length/2)),
                 mergeSort(Arrays.copyOfRange(a, a.length/2, a.length)));
  }


  public static void main(String[] args) {
    int[] a = new int[]{10, 9, 8, 3, 4, 5, 2, 1, 0, 11, 12, 2, 7};
    Integer[] a2 = new Integer[]{10, 9, 8, 3, 4, 5, 2, 1, 0, 11, 12, 2, 7};
    LinkedList<Integer> l = new LinkedList<Integer>(Arrays.asList(a2));
    System.out.println(Arrays.toString(a));
    System.out.println(Arrays.toString(mergeSort(a)));
    System.out.println(mergeSort(l));
  }
}
