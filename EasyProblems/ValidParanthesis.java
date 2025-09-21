package EasyProblems;

import java.util.HashMap;
import java.util.LinkedList;

public class ValidParanthesis {

    public static boolean isValid(String s) {

        LinkedList<String> stack = new LinkedList<>();

        HashMap<String, String> paranthesisMap = new HashMap<>();

        paranthesisMap.put(")", "(");
        paranthesisMap.put("}", "{");
        paranthesisMap.put("]", "[");

        int iterator = 0;
        String top;
        char curr;

        while(iterator < s.length()) {

            curr = s.charAt(iterator);

            if(stack.size() == 0) {

                stack.add(String.valueOf(curr));
                iterator += 1;
                continue;

            }

            top = stack.get(stack.size() - 1);

            System.out.println("Stack :" +  stack);

            String complement = paranthesisMap.get(String.valueOf(curr));

            if( !top.equals(complement)) {
                stack.addFirst(String.valueOf(curr));
            }
            else {
                stack.removeFirst();
            }

            iterator += 1;

        }

        if(stack.size() == 0) {
            return true;
        }

        return false;
    }

    public static void main(String args[]) {
        System.out.println(isValid("()[]{}"));
    }

}
