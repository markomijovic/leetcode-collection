class Solution {
    public boolean isPossible(int[] target) {
        PriorityQueue<Integer> pq =new PriorityQueue<>((x, y) -> Integer.compare(y, x));
        int sum = 0;
        for (int num : target) {
            sum += num;
            pq.add(num);
        }
        while (pq.peek() != 1) {
            int max = pq.poll();
            sum -= max; // sum of the other elements
            if (max <= sum || sum < 1) {
                return false;
            }
            int prev_val = max % sum; // value before we added sum to it
            sum += prev_val; // sum of all the elements pre adding to the new max
            pq.add(prev_val > 0 ? prev_val : sum);
        }
        return true;
    }
}