package MediumProblems;

public class ZigzagConversion {

    public static String convert(String s, int numRows) {

        int iterator = 0;
        int jumper;

        int jumpMargin = (numRows-1) * 2;
        int tempJumpMargin = jumpMargin;

        StringBuilder convertedString = new StringBuilder();

        while(iterator <= numRows - 1) {

            jumper = iterator;
            boolean flipBit = false;
            while (jumper <= s.length() - 1) {
                convertedString.append(s.charAt(jumper));
                if (flipBit) {
                    jumper += jumpMargin - (tempJumpMargin);
                    flipBit = false;
                }
                else{
                    jumper += tempJumpMargin;
                    if(iterator != 0 && iterator!= numRows-1){
                        flipBit = true;
                    }
                }

            }

            if(iterator < numRows - 1) {
                tempJumpMargin -= 2;
            }

            if(tempJumpMargin == 0) {
                tempJumpMargin = jumpMargin;
            }

            iterator++;
        }

        return convertedString.toString();
    }

    public static void main(String args[]) {
        System.out.println(convert("PAYPALISHIRING", 4));
    }
}
