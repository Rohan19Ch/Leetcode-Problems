package MediumProblems;

import java.util.Arrays;

class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {

        int iterator = 0;

        String longestPrefix = "";

        Arrays.sort(strs);

        while(iterator < strs[0].length() && strs[0].charAt(iterator) == strs[strs.length - 1].charAt(iterator)) {

            iterator += 1;
        }

        return strs[0].substring(0, iterator);

    }

    public static void main(String args[]){

    }

}