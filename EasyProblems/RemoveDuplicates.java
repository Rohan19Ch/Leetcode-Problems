package EasyProblems;

public class RemoveDuplicates {

    public int removeDuplicates(int[] nums) {

        int initial = 0;
        int iterator = 0;

        while(iterator < nums.length) {

            if (nums[initial] != nums[iterator]) {

                nums[initial + 1] = nums[iterator];
                initial += 1;
            }

            iterator += 1;
        }

        return initial + 1;
    }

}
