package MediumProblems;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {

    public static List<List<Integer>> threeSum(int[] nums) {


        // Create an empty list to add all the triplets we find
        List<List<Integer>> answer = new ArrayList<>();

        //sort the array to make it easy for two pointer approach
        Arrays.sort(nums);

        for(int outer = 0; outer < nums.length - 2; outer++) { // start with the first element, and iterate up to the third last element

            /**
             * If the outer iterator's number goes beyond 0, there is no way we find any more triplets, since the array is sorted.
             * This also takes care of the case where the array only has positive elements, in which case, the function will just return an empty array
             */
            if(nums[outer] > 0) {
                break;
            }

            //This condition takes care of any duplicates for the outer loop. We should skip any number that we just processed: -
            if(outer > 0 && nums[outer] == nums[outer - 1]){
                continue;
            }

            //We move from the number to the right of the outer loop, till the end of the array to find relevant triplets
            int innerLeft = outer + 1;
            int innerRight = nums.length - 1;

            //We'll move the inner pointers as long as the left pointer does not cross the right pointer
            while(innerLeft < innerRight) {


                int sum = nums[innerLeft] + nums[innerRight]  + nums[outer];
                if( sum < 0) { // If the sum is less than zero, we need to decrease the difference, hence a rightward movement

                    innerLeft++;

                } else if(sum > 0) {  // If the sum is greater than zero, we need to decrease the difference, hence a leftward movement

                    innerRight--;

                } else{ // Above two conditions failing means we get our triplet, and we add it to the list of answers

                    answer.add(Arrays.asList(nums[outer], nums[innerLeft], nums[innerRight]));

                    /**
                     * The below two while blocks take care of any inner duplicates. No point in processing same numbers to find relevant triplets
                     */
                    while(innerLeft < innerRight && nums[innerLeft] == nums[innerLeft + 1]) {
                        innerLeft++;
                    }

                    while(innerLeft < innerRight && nums[innerRight] == nums[innerRight - 1]){
                        innerRight--;
                    }

                    innerLeft++;
                    innerRight--;

                }
            }
        }

        return answer;

    }

    public  static void main(String args[]) {

        int[] nums = {-1,0,1,2,-1,-4};
        System.out.println(threeSum(nums));
    }
}
