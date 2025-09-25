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
