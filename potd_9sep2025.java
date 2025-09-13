/*Assign Mice Holes
You are given two arrays mices[] and holes[] of the same size. The array mices[] represents the positions of the mice on a straight line, while the array holes[] represents the positions of the holes on the same line. Each hole can accommodate exactly one mouse. A mouse can either stay in its current position, move one step to the right, or move one step to the left, and each move takes one minute. The task is to assign each mouse to a distinct hole in such a way that the time taken by the last mouse to reach its hole is minimized.

Examples:
Input: mices[] = [4, -4, 2], holes[] = [4, 0, 5] 
Output: 4
Explanation: Assign the mouse at position 4 to the hole at position 4, so the time taken is 0 minutes. Assign the mouse at position −4 to the hole at position 0, so the time taken is 4 minutes. Assign the mouse at position 2 to the hole at position 5, so the time taken is 3 minutes. Hence, the maximum time required by any mouse is 4 minutes.

Input: mices[] = [1, 2], holes[] = [20, 10] 
Output: 18 
Explanation: Assign the mouse at position 1 to the hole at position 10, so the time taken is 9 minutes. Assign the mouse at position 2 to the hole at position 20, so the time taken is 18 minutes. Hence, the maximum time required by any mouse is 18 minutes.

Constraints:
1 ≤ mices.size() = holes.size() ≤ 105
-105 ≤ mices[i] , holes[i] ≤ 10

Expected Complexities
Time Complexity: O(n log n)
Auxiliary Space: O(1)
 */
import java.util.Arrays;
public class potd_9sep2025 {
     public static int assignHole(int[] mice, int[] holes) {
        /* Sort the arrays */
        Arrays.sort(mice);
        Arrays.sort(holes);

        int n = mice.length;

        /* finding max difference between ith mice and hole */
        int max = 0;
        for (int i = 0; i <n; i++)
            if (max < Math.abs(mice[i] - holes[i]))
                max = Math.abs(mice[i] - holes[i]);

        return Math.abs(max);
    }

    public static void main(String[] args) {
        potd_9sep2025 output = new potd_9sep2025();
        int[] mice = {4, -4, 2};
        int[] holes = {4, 0, 5};
        System.out.println(output.assignHole(mice, holes));
    }
}
