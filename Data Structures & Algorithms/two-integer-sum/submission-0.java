class Solution {
    public int[] twoSum(int[] nums, int target) {
        int num1;
        int num2;
        int[] arr = new int[2];

        HashMap<Integer, Integer> find = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            num1 = i;

            if (find.containsKey(target - nums[i]))
                {
                    num2 = find.get((target-nums[i]));
                    arr[1] = num1;
                    arr[0] = num2;
                    return arr;
                }

            find.put(nums[i], i);
        }
        return arr;
    }
}
