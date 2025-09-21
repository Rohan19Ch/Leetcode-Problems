package MediumProblems;

public class ContainerWithMostWater {

    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;

        int maxArea = 0;
        int currArea = 0;

        while( left < right ) {
            currArea = Math.min(height[left], height[right]) * (right - left);
            if(currArea > maxArea) {
                maxArea = currArea;
            }

            if(height[left] < height[right]) {
                left ++;
            } else if (height[left] >= height[right]) {
                right--;
            }
        }

        return maxArea;
    }
}
