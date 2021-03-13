// import java.util.ArrayList;

class Solution {

    // input: [1,2,3,4,5,6,7]
    // input: [a,b,c,d,e,f,g]

    // last element goes 1 * k, displaced element bumps up by 3
    // store in temp the lost element
    // second last element goes 1 * (k-1), displaced element bumps up by 3

    // displacedNums = { 4 : 3,  }
    // [7,2,3,1,5,6,7]

    // output: [5,6,7,1,2,3,4]
    
    
    // time: O(N)
    // space: O(N)
    // [5, 6, 7, 1, 2, 3, 4]
    
    // case 1: nums = [1,2,3,4,5,6,7], k = 4
    // [1,2,3,4,5,6,7]
    // currRotatedNum = 4
    // [4, 5, 6, 7, 1, 2, 3]
    
    // edge cases:
    // 1 element array:
    // [3] k = 0
    // 2 element array:
    // if k > nums:
    // [4, 5, 6, 7] k = 7
    // [5, 6, 7, 4]
    // size == k:
    // [4, 5, 6, 7] k = 4 (works)
    
    
    // [1,2,3,4,5,6,7]
    
    // replace i+1 by ith elemnent
    
    // [_,1,2,3,4,5,6]
    
    // int stage = a[0]
    // 
    // [_, 1]
    // stage = 2
    // [_, 1,2, ]
    // stage = 3
    
    // stage = 7
    // [_, 1,2,3,4,5,6]
    // a[0] = stage
    
    // [7,1,2,3,4,5,6]
    
    // for i in rage (0, k) rotate1(a); // O(kn)

    // 6+3 % 7 = 2
    public void rotate(int[] nums, int k) {
      for(int i = 0; i < k; ++i) this.shiftElementsUp(nums);
    }
    
  public void shiftElements1(int[] nums) {
    int stage = nums[0];
    // shifting up elements
    for (int i = 1; i < nums.length; ++i) {
        // swap(stage, nums[i])
        int temp = nums[i];
        nums[i] = stage;
        stage = temp;
    }
        nums[0] = stage;
    }
    /**
     * shift nums up by 1 and puts last element at front
     * mutate nums to stay O(1) space complexity
     */
    
    public void shiftElementsUp(int[] nums) {
        int temp = nums[nums.length - 1];
        // shifting up elements
        for (int i = nums.length - 1; i > 0; --i) {
            nums[i] = nums[i-1];
        }
        // replace first element with previous last
        nums[0] = temp;
    } 
}

