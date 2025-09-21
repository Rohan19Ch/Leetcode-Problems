package MediumProblems;

import java.lang.Math;

public class ReverseInteger {

    public int reverse(int x) {

        int reversed = 0;
        boolean isNegative = false;

        if(x<0) {
            isNegative = true;
        }

        x = Math.abs(x);

        while(x>0) {
            reversed += x%10;
            x = x/10;
        }

        return 2;



    }
}
