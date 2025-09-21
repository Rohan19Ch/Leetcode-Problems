package EasyProblems;

public class RemoveElementsInPlace {

    public int removeElement(int[] nums, int val) {

        int initial = 0;
        int iterator = 0;
        int temp;

        while(iterator < nums.length) {

            if(nums[iterator] == val && initial != iterator) {
                temp = nums[initial];
                nums[initial] = nums[iterator];
                nums[iterator] = temp;
                initial++;
            }

            iterator++;

        }

        return initial;

    }

}
