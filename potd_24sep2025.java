/*Design MinMax Queue

Design a SpecialQueue data structure that functions like a normal queue but with additional support for retrieving the minimum and maximum element efficiently.
The SpecialQueue must support the following operations:

enqueue(x): Insert an element x at the rear of the queue.
dequeue(): Remove the element from the front of the queue.
getFront(): Return the front element without removing.
getMin(): Return the minimum element in the queue in O(1) time.
getMax(): Return the maximum element in the queue in O(1) time.
There will be a sequence of queries queries[][]. The queries are represented in numeric form:

1 x : Call enqueue(x)
2:  Call dequeue()
3: Call getFront()
4: Call getMin()
5: Call getMax()
The driver code will process the queries, call the corresponding functions, and print the outputs of getFront(), getMin(), getMax() operations.
You only need to implement the above five functions.

Note: It is guaranteed that all the queries are valid.

Examples:
Input: q = 6, queries[][] = [[1, 4], [1, 2], [3], [4], [2], [5]]
Output: [4, 2, 2]
Explanation: Queries on queue are as follows:
enqueue(4): Insert 4 at the rear of the queue.
enqueue(2): Insert 2 at the rear of the queue.
return the front element i.e 4
return minimum element from the queue i.e 2
dequeue(): Remove the front element 4 from the queue
return maximum element from the queue i.e 2

Input: q = 4, queries[][] = [[1, 3], [4], [1, 5], [5]]
Output: [3, 5]
Explanation: Queries on queue are as follows:
enqueue(3): Insert 3 at the rear of the queue.
return minimum element from the queue i.e 3
enqueue(5): Insert 5 at the rear of the queue.
return maximum element from the queue i.e 5
Constraints:
1 ≤ queries.size() ≤ 105
0 ≤ values in the queue ≤ 109

Expected Complexities
Time Complexity: O(1)
Auxiliary Space: O(n)*/
import java.util.LinkedList;
import java.util.Queue;

public class potd_24sep2025 {
    Queue<Integer> q = new LinkedList<Integer>();
	int max = Integer.MIN_VALUE;
	int min = Integer.MAX_VALUE;

    public void enqueue(int x) {
        // Insert element into the queue
        if (x>max) {
			max = x;
		}
		if (x<min) {
			min = x;
		}
		q.add(x);
    }

    public  void dequeue() {
        // Remove element from the queue
        int removeElement = q.remove();
		if (q.isEmpty()) {
			max = Integer.MIN_VALUE;
			min = Integer.MAX_VALUE;
			return;
		}
		if (removeElement == min) {
			min = Integer.MAX_VALUE;
			q.forEach(value -> {
				if (value < min) {
					min = value;
				}
			});
		}
		if (removeElement == max) {
			max = Integer.MIN_VALUE;
			q.forEach(value -> {
				if (value > max) {
					max = value;
				}
			});
		}
    }

    public   int getFront() {
        // Get front element
        return q.peek();
    }

    public  int getMin() {
        // Get minimum element
        return min;
    }

    public int getMax() {
        // Get maximum element
        return max;
    }
    public static void main(String[] args) {
        potd_24sep2025 q = new potd_24sep2025();
        q.enqueue(4);
        q.enqueue(2);
        q.enqueue(1);
        System.out.print(q.getMin() + " ");   
        q.enqueue(6);
        q.dequeue();                  
        System.out.print(q.getFront() + " "); 
        System.out.print(q.getMin() + " ");   
    }
}
