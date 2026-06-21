class Solution {
    public boolean hasDuplicate(int[] nums) {
        int n = nums.length;
        HashSet<Integer> h = new HashSet<>();
        for(int i = 0;i<n;i++){
            if(!h.contains(nums[i])){
                h.add(nums[i]);
            }
        }
        if (h.size()!=nums.length){
            return true;
        }
        else
        {
            return false;    
        }







    }
}